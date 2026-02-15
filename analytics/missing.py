import csv, os, re

natsort = lambda x: [int(c) if c.isdigit() else c.lower() for c in re.split('([0-9]+)', x)]

reader = csv.DictReader(open('daily.csv','r'))

daily = set(f'{r['questionFrontendId']}.{r['titleSlug']}.py' for r in reader)

files = set(filter(lambda s:re.search(r'^([\d]+)\..*\.py$',s), os.listdir('../leetcode')))

missing = daily-files

missing = sorted(missing, key=natsort)

f = open('missing.csv', 'w', newline='')
writer = csv.DictWriter(f, ['name', 'url'])
writer.writeheader()

os.makedirs("templates", exist_ok=True)

rows = []

for name in missing:
    url = 'https://leetcode.com/problems/' + name.split('.')[1]
    rows.append({'name':name, 'url': url})

    f = open(os.path.join('templates', name), 'w')
    f.write(f"from lc import *\n\n# {url}\n\ntest('''\n\n''')\n")

writer.writerows(rows)
