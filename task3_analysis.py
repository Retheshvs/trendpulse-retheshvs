import json

def analyze_data():
    with open("data_processed.json", "r") as f:
        data = json.load(f)

    total_titles = len(data)
    avg_length = sum(item["length"] for item in data) / total_titles

    longest_title = max(data, key=lambda x: x["length"])

    result = {
        "total_titles": total_titles,
        "average_length": avg_length,
        "longest_title": longest_title
    }

    with open("analysis_result.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Analysis done!")

if __name__ == "__main__":
    analyze_data()