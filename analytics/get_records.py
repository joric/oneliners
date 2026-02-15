import csv
import json
import time
import os
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Configuration
DAILY_FILENAME = "daily.csv"
WEEKLY_FILENAME = "weekly.csv"
BASE_URL = "https://leetcode.com/graphql/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; PythonScript/1.0)",
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/",
}
FIELDNAMES = ["date", "titleSlug", "questionFrontendId", "title", "difficulty", "acRate"]

def get_last_date(filename):
    """Reads the last date from an existing CSV file."""
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            # We use a generator to find the last line without loading the whole file
            reader = csv.DictReader(f)
            last_row = None
            for row in reader:
                last_row = row
            return last_row['date'] if last_row else None
    except Exception:
        return None

def fetch_month_data(year, month):
    """Fetches LeetCode challenge data for a specific year and month using POST."""
    
    # GraphQL query defined exactly as LeetCode expects it
    query = """
    query dailyCodingChallengeV2($year: Int!, $month: Int!) {
        dailyCodingChallengeV2(year: $year, month: $month) {
            challenges {
                date
                question {
                    questionFrontendId
                    title
                    titleSlug
                    difficulty
                    stats
                }
            }
            weeklyChallenges {
                date
                question {
                    questionFrontendId
                    title
                    titleSlug
                    difficulty
                    stats
                }
            }
        }
    }
    """
    
    payload = {
        "query": query,
        "variables": {"year": year, "month": month}
    }

    try:
        response = requests.post(BASE_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        
        data = response.json()
        if "errors" in data:
            print(f"GraphQL Error for {year}-{month}: {data['errors']}")
            return None
            
        return data.get("data", {}).get("dailyCodingChallengeV2", {})
        
    except requests.exceptions.RequestException as e:
        print(f"Network Error fetching {year}-{month}: {e}")
        return None

def process_challenge(item):
    """Parses a single challenge item."""
    if not item or not item.get("question"):
        return None

    q = item["question"]
    stats_str = q.get("stats", "{}")
    # stats is a JSON string inside the JSON response
    stats = json.loads(stats_str) if stats_str else {}
    
    return {
        "date": item["date"],
        "titleSlug": q.get("titleSlug", ""),
        "questionFrontendId": q.get("questionFrontendId", ""),
        "title": q.get("title", ""),
        "difficulty": q.get("difficulty", ""),
        "acRate": stats.get("acRate", "").replace("%", "")
    }

def append_to_csv(filename, items):
    """Appends unique items to CSV."""
    if not items:
        return

    file_exists = os.path.exists(filename)
    
    # Simple deduplication: Check existing dates if file exists
    existing_dates = set()
    if file_exists:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_dates.add(row['date'])

    new_items = [i for i in items if i['date'] not in existing_dates]
    
    if not new_items:
        return

    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()
        writer.writerows(new_items)
        print(f" -> Added {len(new_items)} rows to {filename}")

def main():
    # 1. Determine Start Date
    last_date_str = get_last_date(DAILY_FILENAME)
    
    if last_date_str:
        start_date = datetime.strptime(last_date_str, "%Y-%m-%d")
        # Start from the same month to ensure we catch any missed days in that month
        start_date = start_date.replace(day=1)
        print(f"Resuming check from {start_date.strftime('%Y-%m')}")
    else:
        start_date = datetime(2020, 4, 1)
        print("No existing data found. Starting from 2020-04")

    # 2. Loop until current month
    end_date = datetime.now()
    current_date = start_date
    
    while (current_date.year < end_date.year) or \
          (current_date.year == end_date.year and current_date.month <= end_date.month):
        
        print(f"Fetching: {current_date.year}-{current_date.month}")
        
        data = fetch_month_data(current_date.year, current_date.month)
        
        if data:
            daily_raw = data.get("challenges", [])
            weekly_raw = data.get("weeklyChallenges", [])

            daily_rows = [process_challenge(c) for c in daily_raw if c]
            weekly_rows = [process_challenge(c) for c in weekly_raw if c]

            append_to_csv(DAILY_FILENAME, daily_rows)
            append_to_csv(WEEKLY_FILENAME, weekly_rows)
        else:
            print(f"No data returned for {current_date.year}-{current_date.month}")

        current_date += relativedelta(months=1)
        time.sleep(2)

    print("Finished updating.")

if __name__ == "__main__":
    main()
