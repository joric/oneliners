import csv
import json
import collections
from datetime import datetime
import os
import statistics

# Configuration
INPUT_FILE = "daily.csv"
OUTPUT_FILE = "../index.html"
LEETCODE_BASE_URL = "https://leetcode.com/problems/"

def load_data(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def get_stats(rows):
    questions = {}
    last_appearance = {}
    recur_times = []
    counts = collections.defaultdict(int)
    
    # Existing stats structures
    diff_map = {"Easy": 0, "Medium": 1, "Hard": 2}
    heatmap_data = [[0]*7 for _ in range(3)] 
    diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}

    for row in rows:
        d_obj = parse_date(row["date"])
        q_id = row["questionFrontendId"]
        difficulty = row["difficulty"]
        
        day_idx = (d_obj.weekday() + 1) % 7 # 0=Sun
        
        # 1. Heatmap & Pie Data
        if difficulty in diff_map:
            r = diff_map[difficulty]
            heatmap_data[r][day_idx] += 1
            diff_counts[difficulty] += 1

        # 2. Recurrence Data
        if q_id in last_appearance:
            delta = (d_obj - last_appearance[q_id]).days
            recur_times.append(delta)
        
        counts[q_id] += 1
        last_appearance[q_id] = d_obj

    # Normalize heatmap
    heatmap_percents = [[0.0]*7 for _ in range(3)]
    for r in range(3):
        row_total = sum(heatmap_data[r])
        if row_total > 0:
            for c in range(7):
                heatmap_percents[r][c] = round((heatmap_data[r][c] / row_total) * 100, 2)

    freq_counts = collections.Counter(counts.values())
    
    # Summary Statistics
    total_days = len(rows)
    unique_questions = len(counts)
    
    avg_recurrence = 0
    if recur_times:
        avg_recurrence = round(statistics.mean(recur_times))
        
    max_freq = max(freq_counts.keys()) if freq_counts else 0
    count_at_max = freq_counts[max_freq] if max_freq else 0

    summary = {
        "total_days": total_days,
        "unique_questions": unique_questions,
        "avg_recurrence": avg_recurrence,
        "max_freq_count": count_at_max,
        "max_freq_apps": max_freq
    }
    
    return {
        "diff_counts": diff_counts,
        "heatmap": heatmap_percents, 
        "recur_times": recur_times,
        "freq_counts": dict(freq_counts),
        "summary": summary
    }

def generate_calendar_html(calendar_data):
    html_parts = []
    sorted_months = sorted(calendar_data.keys(), key=lambda x: datetime.strptime(x, "%B %Y"), reverse=True)

    for month_str in sorted_months:
        days_data = calendar_data[month_str]
        dt = datetime.strptime(month_str, "%B %Y")
        start_day_idx = (dt.replace(day=1).weekday() + 1) % 7
        
        import calendar
        _, num_days = calendar.monthrange(dt.year, dt.month)
        
        month_html = f"""
        <div class="month-card">
            <div class="month-header">{month_str}</div>
            <div class="days-container">
                <div class="day-name">Sun</div><div class="day-name">Mon</div><div class="day-name">Tue</div>
                <div class="day-name">Wed</div><div class="day-name">Thu</div><div class="day-name">Fri</div><div class="day-name">Sat</div>
        """
        for _ in range(start_day_idx):
            month_html += '<div class="day-cell empty"></div>'
        for day in range(1, num_days + 1):
            if day in days_data:
                info = days_data[day]
                diff_class = info['diff']
                #link = f"{LEETCODE_BASE_URL}{info['slug']}/"
                link = f"https://raw.githubusercontent.com/joric/oneliners/refs/heads/main/leetcode/{info['id']}.{info['slug']}.py"
                tooltip = f"{info['id']}. {info['title']}"
                month_html += f'<div class="day-cell {diff_class}" title="{tooltip}"><a href="{link}" target="_blank">{day}</a></div>'
            else:
                month_html += f'<div class="day-cell empty">{day}</div>'
        month_html += "</div></div>"
        html_parts.append(month_html)
    return "\n".join(html_parts)

def generate_html(rows, stats):
    calendar_data = collections.defaultdict(lambda: collections.defaultdict(dict))
    for row in rows:
        d = parse_date(row["date"])
        year_month = d.strftime("%B %Y")
        calendar_data[year_month][d.day] = {
            "title": row["title"], "slug": row["titleSlug"], 
            "diff": row["difficulty"], "id": row["questionFrontendId"]
        }

    json_stats = json.dumps(stats)
    calendar_block = generate_calendar_html(calendar_data)
    
    s = stats["summary"]
    summary_text = (f"{s['max_freq_count']} questions appeared {s['max_freq_apps']} times. "
                    f"Out of {s['total_days']} total days, there were {s['unique_questions']} unique questions.<br>"
                    f"Average time between reoccurrences: {s['avg_recurrence']} days.")
    
    github_corner = """
<a href="https://github.com/joric/oneliners/" target="_blank" class="github-corner" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"/><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"/><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"/></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>
    """

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeetCode Daily History</title>
    <script src="https://cdn.plot.ly/plotly-2.24.1.min.js"></script>
    <style>
        * {{ box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #f4f6f8; margin: 0; padding: 20px; }}
        .container {{ max_width: 1400px; margin: 0 auto; }}
        
        .header-section {{ text-align: center; margin-bottom: 40px; }}
        h1 {{ color: #333; margin-bottom: 10px; }}
        .summary-text {{ font-size: 1.1em; color: #555; line-height: 1.5; }}
        
        /* --- Chart Grid System --- */
        .stats-grid {{ 
            display: grid; 
            grid-template-columns: 1fr 1fr; 
            gap: 20px; 
            margin-bottom: 40px; 
        }}
        
        .chart-card {{ 
            background: white; 
            padding: 10px; 
            border-radius: 8px; 
            box-shadow: 0 2px 5px rgba(0,0,0,0.1); 
            height: 450px; 
            width: 100%;
            overflow: hidden;
        }}
        
        .full-width {{ grid-column: 1 / -1; }}

        /* --- Calendar Grid System --- */
        .calendar-grid {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); 
            gap: 20px; 
        }}
        
        .month-card {{ background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); overflow: hidden; display: flex; flex-direction: column; }}
        .month-header {{ background: #2c3e50; color: white; padding: 15px; text-align: center; font-weight: bold; font-size: 1.1em; }}
        .days-container {{ display: grid; grid-template-columns: repeat(7, 1fr); padding: 10px; gap: 2px; }}
        .day-name {{ text-align: center; font-size: 0.85em; color: #777; padding-bottom: 10px; font-weight: 600; }}
        .day-cell {{ aspect-ratio: 1 / 1; border: 1px solid #f0f0f0; display: flex; align-items: center; justify-content: center; font-size: 0.95em; cursor: pointer; border-radius: 4px; transition: transform 0.1s ease; }}
        .day-cell:hover:not(.empty) {{ transform: scale(1.1); z-index: 2; box-shadow: 0 4px 8px rgba(0,0,0,0.15); }}
        .day-cell a {{ text-decoration: none; color: inherit; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; }}
        .day-cell.empty {{ background: transparent; border: none; cursor: default; }}
        
        .Easy {{ background-color: #00b8a3; color: white; border-color: #00b8a3; }}
        .Medium {{ background-color: #ffc01e; color: black; border-color: #ffc01e; }}
        .Hard {{ background-color: #ff375f; color: white; border-color: #ff375f; }}
        
        @media (max-width: 900px) {{
            .stats-grid {{ grid-template-columns: 1fr; }}
            .chart-card {{ height: 350px; }}
            .calendar-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header-section">
            <h1>LeetCode Daily Stats & Calendar</h1>
            <div class="summary-text">{summary_text}</div>
        </div>
        
        <div class="stats-grid">
            <div class="chart-card"><div id="pieChart"></div></div>
            <div class="chart-card"><div id="freqChart"></div></div>
            <div class="chart-card full-width"><div id="heatmapChart"></div></div>
            <div class="chart-card full-width"><div id="recurChart"></div></div>
        </div>

        <div class="calendar-grid">
            {calendar_block}
        </div>
    </div>
    
    {github_corner}

    <script>
        const stats = {json_stats};
        
        const commonLayout = {{
            autosize: true, 
            margin: {{ t: 40, b: 80, l: 40, r: 40 }},
        }};
        
        const config = {{ responsive: true, displayModeBar: false }};

        // --- 1. Pie Chart ---
        Plotly.newPlot('pieChart', [{{
            values: [stats.diff_counts.Easy, stats.diff_counts.Medium, stats.diff_counts.Hard],
            labels: ['Easy', 'Medium', 'Hard'],
            type: 'pie',
            marker: {{ colors: ['#00b8a3', '#ffc01e', '#ff375f'] }}
        }}], {{ ...commonLayout, title: 'Daily Question Distribution' }}, config);

        // --- 2. Frequency Bar Chart ---
        const freqKeys = Object.keys(stats.freq_counts).map(Number).sort((a,b)=>a-b);
        Plotly.newPlot('freqChart', [{{
            x: freqKeys,
            y: freqKeys.map(k => stats.freq_counts[k]),
            type: 'bar',
            marker: {{ color: '#448aff' }}
        }}], {{
            ...commonLayout, title: 'Question Frequency (Appearances)',
            xaxis: {{title: 'Appearances'}}, yaxis: {{title: '# Questions'}}
        }}, config);

        // --- 3. Heatmap ---
        const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        const diffs = ['Easy', 'Medium', 'Hard'];
        let annotations = [];
        for (let i=0; i<3; i++) {{
            for (let j=0; j<7; j++) {{
                annotations.push({{
                    xref: 'x1', yref: 'y1', x: days[j], y: diffs[i],
                    text: stats.heatmap[i][j] + '%',
                    font: {{ color: stats.heatmap[i][j] > 50 ? 'white' : 'black' }}, showarrow: false
                }});
            }}
        }}
        Plotly.newPlot('heatmapChart', [{{
            z: stats.heatmap, x: days, y: diffs, type: 'heatmap', colorscale: 'Teal', showscale: true
        }}], {{ ...commonLayout, title: 'Difficulty Day Frequency (%)', annotations: annotations }}, config);

        // --- 4. Recurrence Histogram ---
        Plotly.newPlot('recurChart', [{{
            x: stats.recur_times, type: 'histogram', marker: {{ color: '#448aff' }}, xbins: {{ size: 30 }}
        }}], {{
            ...commonLayout, title: 'Time for question to reoccur (Days)',
            xaxis: {{title: 'Days Between Appearances'}}, yaxis: {{title: 'Count'}}
        }}, config);

    </script>
</body>
</html>
    """
    return html

def main():
    rows = load_data(INPUT_FILE)
    if not rows: return
    stats = get_stats(rows)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f: f.write(generate_html(rows, stats))
    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
