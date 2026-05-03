import csv
import collections
from datetime import datetime

# Configuration
INPUT_FILE = "daily.csv"

def parse_date(date_str):
    """Parses YYYY-MM-DD string to datetime object."""
    return datetime.strptime(date_str, "%Y-%m-%d")

def main():
    rows = []
    
    # Read CSV
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return

    if not rows:
        print("No data found.")
        return

    # Data Structures
    questions = {} # ID -> Display String
    last_appearance = {} # ID -> Date Object
    recur_times = [] # List of timedeltas
    min_occurences = {} # ID -> (timedelta, start_date, end_date)
    counts = collections.defaultdict(int) # ID -> Count
    
    # Initialize Difficulty Stats
    diff_types = ["Easy", "Medium", "Hard"]
    diff_stats = {
        d: {"count": 0, "day": [0]*7} for d in diff_types
    }

    # Process Rows
    for row in rows:
        date_obj = parse_date(row["date"])
        q_id = row["questionFrontendId"]
        title = row["title"]
        difficulty = row["difficulty"]
        
        # Note: Javascript's getUTCDay() returns 0 for Sunday. 
        # Python's weekday() returns 0 for Monday. 
        # To match JS output (Sunday=0), we use isoweekday() % 7
        day_of_week = date_obj.isoweekday() % 7 

        # Difficulty Stats
        if difficulty in diff_stats:
            diff_stats[difficulty]["count"] += 1
            diff_stats[difficulty]["day"][day_of_week] += 1

        # Question mapping
        questions[q_id] = f"{q_id}. {title} ({difficulty})"

        # Recurrence Logic
        if q_id in last_appearance:
            prev_date = last_appearance[q_id]
            delta = date_obj - prev_date
            
            if q_id not in min_occurences or delta < min_occurences[q_id][0]:
                min_occurences[q_id] = (delta, prev_date, date_obj)
            
            recur_times.append(delta)

        counts[q_id] += 1
        last_appearance[q_id] = date_obj

    # Post-Processing
    count_of_counts = collections.Counter(counts.values())
    total_rows = len(rows)
    unique_qs = len(questions)
    reoccurred_qs = len(min_occurences)
    
    avg_recur_days = 0
    if recur_times:
        total_seconds = sum(t.total_seconds() for t in recur_times)
        avg_recur_days = total_seconds / (len(recur_times) * 24 * 3600)

    # --- Output ---
    print("\nGeneral Stats\n=======")
    print(f"Total dailies: {total_rows}")
    print(f"Unique questions: {unique_qs}")
    print(f"Number of questions that reoccurred: {reoccurred_qs}")
    print(f"Avg. Recur Time: {avg_recur_days:.2f} Days")

    print("\nDifficulty Count\n=======")
    for diff in diff_types:
        count = diff_stats[diff]["count"]
        percent = (count / total_rows * 100) if total_rows > 0 else 0
        print(f"{diff:<7}: {count} ({percent:.2f}%)")

    print("\nDifficulty Day Frequency\n=======")
    for diff in diff_types:
        d_data = diff_stats[diff]
        total_d = d_data["count"]
        # Map raw counts to percentages
        percents = [
            f"{(x / total_d * 100):.2f}".ljust(7) if total_d > 0 else "0.00   " 
            for x in d_data["day"]
        ]
        print(f"{diff:<7}: {','.join(percents)}")

    print("\nQuestion Frequency\n=======")
    # Sort by number of appearances (keys)
    for num_apps in sorted(count_of_counts.keys()):
        freq = count_of_counts[num_apps]
        plural = "s" if num_apps > 1 else " "
        print(f"{num_apps} Appearance{plural} : {freq} Questions")

    print("\nMinimum time since occurence\n=======")
    # Sort min_occurences by timedelta duration
    sorted_min = sorted(min_occurences.items(), key=lambda item: item[1][0])[:5]

    for q_id, data in sorted_min:
        delta, start, end = data
        days = delta.days
        print(questions[q_id])
        # Format: 10 days : Fri, 01 Jan 2021 - Mon, 11 Jan 2021
        # (Simplified date format compared to raw UTC string, but cleaner)
        print(f"{days} days : {start.strftime('%a, %d %b %Y')} - {end.strftime('%a, %d %b %Y')}\n")

if __name__ == "__main__":
    main()
