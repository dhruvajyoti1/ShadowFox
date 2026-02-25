import pandas as pd

def analyze_players(df, players, output_path):
    # Filter target players
    d = df[df["Player Name"].isin(players)].copy()

    # Event classification
    d["CP"] = d["Pick"].astype(str).str.upper().eq("Y").astype(int)
    d["GT"] = d["Throw"].astype(str).str.upper().eq("Y").astype(int)
    d["RS"] = pd.to_numeric(d["Runs"], errors="coerce").fillna(0)

    # Aggregate by player
    summary = d.groupby("Player Name")[["CP", "GT", "RS"]].sum()

    # Performance Score formula
    summary["PS"] = summary["CP"]*1 + summary["GT"]*2 + summary["RS"]

    # Save summary
    summary.to_csv(output_path)
    print("Summary saved at:", output_path)

    return summary