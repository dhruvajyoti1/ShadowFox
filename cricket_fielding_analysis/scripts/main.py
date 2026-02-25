import os
import pandas as pd
from clean_data import clean_dataset
from analyze_fielding import analyze_players
from visualize import create_charts

# File paths
RAW_DATA_PATH = "../data/fielding_data.xlsx"
CLEAN_DATA_PATH = "../output/cleaned_data.csv"
SUMMARY_PATH = "../output/summary.csv"
CHART_DIR = "../output/charts"

# Create output folders if they don’t exist
os.makedirs("../output/charts", exist_ok=True)

# Step 1: Clean dataset
df_clean = clean_dataset(RAW_DATA_PATH, CLEAN_DATA_PATH)

# Step 2: Define players
players = ["Axar Patel", "Phil Salt", "Rilee Russouw"]

# Step 3: Analyze
summary = analyze_players(df_clean, players, SUMMARY_PATH)

# Step 4: Visualize
create_charts(summary, CHART_DIR)

print("\nFielding Analysis Completed Successfully!")
print("Check the output folder for results.")