import nead
import pandas as pd

# Convert NEAD files to Pandas dataframes
station = pd.read_csv("/metadata/station_info.csv", header=0)
dfs_daily = []

for name, ID in zip(station.Name, station.ID):
    format_name = name.replace(" ", "")
    files = "data_daily/" + str(ID).zfill(2) + "-" + format_name + "_daily.csv"
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
