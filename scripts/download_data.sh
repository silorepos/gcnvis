#!/usr/bin/env bash

# Latest L1 data: https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing/tree/main/L1
# API contents of latest L1 data (raw URLs etc.): https://api.github.com/repositories/319306521/contents/L1

# Prepare directories
cd ..
mkdir -p data data_daily data_hourly

# Download data
echo -ne 'Downloading daily data...\r'
xargs -n 1 curl --silent -O --output-dir data_daily < metadata/urls_1.txt
echo -ne 'Downloading hourly data...\r'
xargs -n 1 curl --silent -O --output-dir data_hourly < metadata/urls_2.txt

# Process data
echo -ne 'Processing daily data...\r'
python scripts/process_data_daily.py
echo -ne 'Processing hourly data...\r'
python scripts/process_data_hourly.py

# Delete unprocessed data
rm -r data_daily data_hourly