
import os
import re
from collections import Counter

import requests
import pandas as pd
import matplotlib.pyplot as plt


# 1. Choose the dates and API endpoint
API_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"

params = {
    "start_date": "2025-01-01",
    "end_date": "2025-01-30"
}

# Create an output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# 2. Retrieve data from NASA
response = requests.get(API_URL, params=params, timeout=30)

# Raise an error if the request was unsuccessful
response.raise_for_status()

data = response.json()

if isinstance(data, dict):
    data = [data]

if not data:
    raise ValueError("The API returned no astronomy records.")

print(f"Retrieved {len(data)} astronomy records.")


# 3. Select useful information
records = []

for item in data:
    records.append({
        "date": item.get("date"),
        "title": item.get("title", "Untitled"),
        "media_type": item.get("media_type", "unknown"),
        "explanation": item.get("explanation", "")
    })

df = pd.DataFrame(records)

# Convert dates to datetime values
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove records without a valid date
df = df.dropna(subset=["date"])

# Save the cleaned dataset
df.to_csv("output/apod_data.csv", index=False)


# 4. Display a useful summary

print("\nFirst five records:")
print(df[["date", "title", "media_type"]].head().to_string(index=False))

print("\nNumber of records by media type:")
print(df["media_type"].value_counts().to_string())

print("\nNumber of records:", len(df))
print("Unique titles:", df["title"].nunique())


# 5. Visualize image vs. video entries

media_counts = df["media_type"].value_counts()

media_counts.plot(kind="bar", rot=0)

plt.title("NASA APOD: Records by Media Type")
plt.xlabel("Media type")
plt.ylabel("Number of records")
plt.tight_layout()
plt.savefig("output/media_types.png", dpi=300)
plt.show()


# 6. Explore astronomy-related keywords

keywords = [
    "galaxy",
    "planet",
    "black holes",
    "star",
    "comet",
    "asteroid",
    "moon",
    "supernova"
]

# Combine each title and explanation for searching
all_text = " ".join(
    (str(row["title"]) + " " + str(row["explanation"]))
    for _, row in df.iterrows()
).lower()

keyword_counts = Counter()

for keyword in keywords:
    # Count occurrences of each keyword
    pattern = r"\b" + re.escape(keyword) + r"\b"
    keyword_counts[keyword] = len(
        re.findall(pattern, all_text)
    )

keyword_series = pd.Series(keyword_counts).sort_values(
    ascending=False
)

print("\nAstronomy keyword counts:")
print(keyword_series.to_string())

# 7. Plot keyword frequencies

keyword_series.sort_values().plot(
    kind="barh"
)

plt.title("Astronomy Keywords in NASA APOD Text")
plt.xlabel("Number of occurrences")
plt.ylabel("Keyword")
plt.tight_layout()
plt.savefig("output/astronomy_keywords.png", dpi=300)
plt.show()

print("\nAnalysis is completed!")
print("CSV and graphs are saved in the output folder.")
