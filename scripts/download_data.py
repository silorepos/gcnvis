#!/usr/bin/env bash

# Latest L1 data: https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing/tree/main/L1
# API contents of latest L1 data (raw URLs etc.): https://api.github.com/repositories/319306521/contents/L1
import os
os.chdir('../')
print(os.getcwd())

try:
	os.mkdir('data')
	os.mkdir('data/data_daily')
	os.mkdir('data/data_hourly')
except:
	print('Overwritting existing data in \"/data\"')
	
import urllib.request

# Download data
print('Downloading daily data...\r')
# xargs -n 1 curl --silent -O --output-dir data_daily < ../metadata/urls_1.txt
for url in open('metadata/urls_1.txt'):
    # Split on the rightmost / and take everything on the right side of that
    name = url.rsplit('/', 1)[-1].replace('\r','')
    # Combine the name and the downloads directory to get the local filename
    filename = os.path.join('data/data_daily', name)

    # Download the file if it does not exist
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(url, filename)
		
print('Downloading hourly data...\r')
# xargs -n 1 curl --silent -O --output-dir data_hourly < ../metadata/urls_2.txt
for url in open('metadata/urls_2.txt'):
    # Split on the rightmost / and take everything on the right side of that
    name = url.rsplit('/', 1)[-1].replace('\r','')

    # Combine the name and the downloads directory to get the local filename
    filename = os.path.join('data/data_hourly', name)

    # Download the file if it does not exist
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(url, filename)
		

# Process data
# echo -ne 'Processing dairly data...\r'
# python scripts/process_data_daily.py
# echo -ne 'Processing hourly data...\r'
# python scripts/process_data_hourly.py

# Delete unprocessed data
# rm -r data_daily data_hourly

# %% process data daily
import pandas as pd
import nead
# Convert NEAD files to Pandas dataframes
station = pd.read_csv("metadata/station_info.csv", header=0)
dfs_daily = []

for name, ID in zip(station.Name, station.ID):
    format_name = name.replace(" ", "")
    files = "data/data_daily/" + str(ID).zfill(2) + "-" + format_name + "_daily.csv"
    ds_daily = nead.read(files, index_col=0)
    df_daily = ds_daily.to_dataframe()
    df_daily.insert(loc=0, column="station_name", value=name)  # Add station_name column to each dataframe
    dfs_daily.append(df_daily)

# Concatenate dataframes
df_daily = pd.concat(dfs_daily).sort_index()

# Delete irrelevant columns from dataframe (i.e. null columns and flag columns)
# null_columns = df_daily.columns[df_daily.isnull().all()]
# flag_columns = df_daily.filter(regex="flag$").columns
# print(null_columns)
# print(flag_columns)

df_daily = df_daily.drop(columns=['OSWR_max', 'HW2_adj_flag', 'P_adj_flag', 'HW1_adj_flag', 'OSWR_adj_flag',
                                  'HS1_adj_flag', 'HS2_adj_flag', 'TA3_adj_flag', 'TA4_adj_flag',
                                  'DW1_adj_flag'])

# Add year column to dataframe
df_daily["year"] = df_daily.index.strftime("%Y")

# Add month column to dataframe
df_daily["month"] = df_daily.index.strftime("%B")

# # Add day column to dataframe
# df_daily["day"] = df_daily.index.strftime("%d")

# Add hour column to dataframe
# df_daily["hour"] = df_daily.index.strftime("%h")

# Add season column to dataframe
seasons = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring",
           6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn",
           11: "Autumn", 12: "Winter"}

# Extract the month from the index and use the dictionary to map it to the corresponding season
df_daily["season"] = df_daily.index.month.map(seasons)


# Save dataframe as parquet file
df_daily.to_parquet("data/df_daily.gzip", compression='gzip')


# %% process data hourly
# Convert NEAD files to Pandas dataframes
station = pd.read_csv("metadata/station_info.csv", header=0)
dfs_hourly = []

for name, ID in zip(station.Name, station.ID):
    format_name = name.replace(" ", "")
    files = "data/data_hourly/" + str(ID).zfill(2) + "-" + format_name + ".csv"
    ds_hourly = nead.read(files, index_col=0)
    df_hourly = ds_hourly.to_dataframe()
    df_hourly.insert(loc=0, column="station_name", value=name)  # Add station_name column to each dataframe
    dfs_hourly.append(df_hourly)

# Concatenate dataframes
df_hourly = pd.concat(dfs_hourly).sort_index()


# Delete irrelevant columns from dataframe (i.e. null columns and flag columns)
# null_columns = df_hourly.columns[df_hourly.isnull().all()]
# flag_columns = df_hourly.filter(regex="flag$").columns
# print(null_columns)
# print(flag_columns)

df_hourly = df_hourly.drop(columns=['OSWR_max', 'HW2_adj_flag', 'P_adj_flag', 'HW1_adj_flag', 'OSWR_adj_flag',
                      'HS1_adj_flag', 'HS2_adj_flag', 'TA3_adj_flag', 'TA4_adj_flag',
                      'DW1_adj_flag'])

# Add year column to dataframe
df_hourly["year"] = df_hourly.index.strftime("%Y")

# Add month column to dataframe
df_hourly["month"] = df_hourly.index.strftime("%B")

# # Add day column to dataframe
# df_hourly["day"] = df_hourly.index.strftime("%d")

# # Add hour column to dataframe
# df_hourly["hour"] = df_hourly.index.strftime("%h")

# Add season column to dataframe
seasons = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring",
           6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn",
           11: "Autumn", 12: "Winter"}

# Extract the month from the index and use the dictionary to map it to the corresponding season
df_hourly["season"] = df_hourly.index.month.map(seasons)

# Save dataframe as parquet file
df_hourly.to_parquet("data/df_hourly.gzip", compression='gzip')