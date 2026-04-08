import pandas as pd
import os

def process_data():
    # Find JSON file inside data folder
    folder = "data"
    files = [f for f in os.listdir(folder) if f.endswith(".json")]

    if not files:
        print("No JSON file found in data folder")
        return

    filepath = os.path.join(folder, files[0])

    # 1️⃣ Load JSON
    df = pd.read_json(filepath)
    print(f"Loaded {len(df)} stories from {filepath}")

    # 2️⃣ Remove duplicates
    df = df.drop_duplicates(subset="post_id")
    print(f"After removing duplicates: {len(df)}")

    # 3️⃣ Remove missing values
    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")

    # 4️⃣ Fix data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # 5️⃣ Remove low quality (score < 5)
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # 6️⃣ Clean whitespace
    df["title"] = df["title"].str.strip()

    # 7️⃣ Save CSV
    output_path = "data/trends_clean.csv"
    df.to_csv(output_path, index=False)

    print(f"\nSaved {len(df)} rows to {output_path}")

    # 8️⃣ Summary (stories per category)
    print("\nStories per category:")
    print(df["category"].value_counts())


if __name__ == "__main__":
    process_data()