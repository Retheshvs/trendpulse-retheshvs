"""
TrendPulse - Task 4: Visualizations
Loads the analysed CSV from Task 3 and creates 3 charts + a bonus dashboard.
All charts are saved as PNG files in the outputs/ folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def load_data():
    """Load the analysed CSV from Task 3."""
    filepath = "data/trends_analysed.csv"
    df = pd.read_csv(filepath)
    print(f"Loaded data: {df.shape}")
    return df


def setup_outputs_folder():
    """Create the outputs/ folder if it doesn't exist."""
    os.makedirs("outputs", exist_ok=True)
    print("outputs/ folder ready.")


def shorten_title(title, max_len=50):
    """Shorten a title to max_len characters, adding '...' if truncated."""
    return title if len(title) <= max_len else title[:max_len] + "..."


# ── Chart 1: Top 10 Stories by Score (horizontal bar chart) ──────────────────
def chart1_top_stories(df):
    """
    Horizontal bar chart of the top 10 stories ranked by score.
    Story titles on the y-axis, score on the x-axis.
    """
    # Get top 10 stories by score
    top10 = df.nlargest(10, "score").copy()
    top10["short_title"] = top10["title"].apply(shorten_title)

    # Sort ascending so highest score appears at the top of the chart
    top10 = top10.sort_values("score", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(top10["short_title"], top10["score"], color="steelblue")

    # Labels and title
    ax.set_xlabel("Score (Upvotes)")
    ax.set_ylabel("Story Title")
    ax.set_title("Top 10 Trending Stories by Score")

    plt.tight_layout()

    # Save BEFORE show (required by assignment)
    plt.savefig("outputs/chart1_top_stories.png", dpi=150)
    print("Saved: outputs/chart1_top_stories.png")
    plt.show()
    plt.close()


# ── Chart 2: Stories per Category (bar chart) ────────────────────────────────
def chart2_categories(df):
    """
    Bar chart showing the number of stories in each category.
    Each bar has a different colour.
    """
    category_counts = df["category"].value_counts()

    # Different colour for each bar
    colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(category_counts.index, category_counts.values, color=colors[:len(category_counts)])

    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Stories")
    ax.set_title("Number of Stories per Category")

    plt.tight_layout()

    plt.savefig("outputs/chart2_categories.png", dpi=150)
    print("Saved: outputs/chart2_categories.png")
    plt.show()
    plt.close()


# ── Chart 3: Score vs Comments (scatter plot) ─────────────────────────────────
def chart3_scatter(df):
    """
    Scatter plot of score (x-axis) vs num_comments (y-axis).
    Popular stories (is_popular=True) are coloured differently.
    """
    # Split into popular and non-popular groups
    popular     = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    fig, ax = plt.subplots(figsize=(9, 6))

    # Plot non-popular first (background), then popular on top
    ax.scatter(not_popular["score"], not_popular["num_comments"],
               color="cornflowerblue", alpha=0.7, label="Not Popular", s=60)
    ax.scatter(popular["score"],     popular["num_comments"],
               color="tomato",       alpha=0.9, label="Popular",     s=80, marker="*")

    ax.set_xlabel("Score (Upvotes)")
    ax.set_ylabel("Number of Comments")
    ax.set_title("Score vs Comments (Popular vs Not Popular)")
    ax.legend()

    plt.tight_layout()

    plt.savefig("outputs/chart3_scatter.png", dpi=150)
    print("Saved: outputs/chart3_scatter.png")
    plt.show()
    plt.close()


# ── Bonus: Dashboard (all 3 charts in one figure) ────────────────────────────
def dashboard(df):
    """
    Combine all 3 charts into a single dashboard figure using subplots.
    Saved as outputs/dashboard.png.
    """
    top10           = df.nlargest(10, "score").copy()
    top10["short_title"] = top10["title"].apply(shorten_title)
    top10           = top10.sort_values("score", ascending=True)

    category_counts = df["category"].value_counts()
    colors          = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]

    popular     = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    # 2 rows x 2 columns; chart 1 spans the full top row
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle("TrendPulse Dashboard", fontsize=18, fontweight="bold", y=1.01)

    # Chart 1 — top row, spans both columns
    ax1 = fig.add_subplot(2, 2, (1, 2))
    ax1.barh(top10["short_title"], top10["score"], color="steelblue")
    ax1.set_xlabel("Score")
    ax1.set_ylabel("Story Title")
    ax1.set_title("Top 10 Stories by Score")

    # Chart 2 — bottom left
    ax2 = fig.add_subplot(2, 2, 3)
    ax2.bar(category_counts.index, category_counts.values,
            color=colors[:len(category_counts)])
    ax2.set_xlabel("Category")
    ax2.set_ylabel("Stories")
    ax2.set_title("Stories per Category")

    # Chart 3 — bottom right
    ax3 = fig.add_subplot(2, 2, 4)
    ax3.scatter(not_popular["score"], not_popular["num_comments"],
                color="cornflowerblue", alpha=0.7, label="Not Popular", s=50)
    ax3.scatter(popular["score"],     popular["num_comments"],
                color="tomato",       alpha=0.9, label="Popular",     s=70, marker="*")
    ax3.set_xlabel("Score")
    ax3.set_ylabel("Comments")
    ax3.set_title("Score vs Comments")
    ax3.legend(fontsize=8)

    plt.tight_layout()

    plt.savefig("outputs/dashboard.png", dpi=150, bbox_inches="tight")
    print("Saved: outputs/dashboard.png")
    plt.show()
    plt.close()


def main():
    print("=== TrendPulse: Task 4 — Visualizations ===\n")

    # Setup
    df = load_data()
    setup_outputs_folder()
    print()

    # Individual charts
    chart1_top_stories(df)
    chart2_categories(df)
    chart3_scatter(df)

    # Bonus dashboard
    dashboard(df)

    print("\nAll charts saved to outputs/")


if __name__ == "__main__":
    main()