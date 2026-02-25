import pandas as pd
import matplotlib.pyplot as plt

def create_charts(summary, output_dir):
    # Event comparison chart
    plt.figure(figsize=(8,6))
    summary[["CP", "GT", "RS"]].plot(kind="bar")
    plt.title("Fielding Event Comparison (CP, GT, RS)")
    plt.ylabel("Count / Runs Saved")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir + "/events_comparison.png")
    plt.close()

    # Performance Score chart
    plt.figure(figsize=(8,6))
    summary["PS"].plot(kind="bar")
    plt.title("Performance Score (PS) by Player")
    plt.ylabel("Performance Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir + "/performance_scores.png")
    plt.close()

    print("Charts saved in /output/charts/")