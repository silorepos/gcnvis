import nead
import pandas as pd

# Convert NEAD files to Pandas dataframes
station = pd.read_csv("/metadata/station_info.csv", header=0)
dfs_hourly = []

for name, ID in zip(station.Name, station.ID):
    format_name = name.replace(" ", "")
    files = "data_hourly/" + str(ID).zfill(2) + "-" + format_name + ".csv"
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
