import pandas as pd

def clean_dataset(input_path, output_path):
    # Load raw dataset
    df = pd.read_excel(input_path, header=None)

    # Clean first 4 rows (legend)
    df2 = df.iloc[4:].copy()

    # Set proper header row
    df2.columns = df2.iloc[0]
    df3 = df2.iloc[1:].copy()

    # Drop empty/unnamed columns
    df3 = df3.drop(columns=[c for c in df3.columns if str(c).startswith("Unnamed")], errors='ignore')

    # Standardize Player Names
    df3["Player Name"] = (
        df3["Player Name"]
        .astype(str)
        .str.title()
        .str.replace("Axer", "Axar")
    )

    # Save cleaned CSV
    df3.to_csv(output_path, index=False)
    print("Cleaned dataset saved at:", output_path)

    return df3