#!/usr/bin/env python3

import urllib.parse
from datetime import datetime

GOOGLE_BASE = "https://www.google.com/search?q="

CAREER_PATHS = ["careers", "jobs", "job"]

# Exclude webpages that don't include job postings/boards.
EXCLUSIONS = [
    "-site:linkedin.com",
    "-site:indeed.com",
    "-site:glassdoor.com",
    "-filetype:pdf",
    "-inurl:blog",
]

RESULTS_HEADER = """# Open these links in your browser tabs to quickly find each company's careers page.
# Tip: Middle-click or Ctrl+Click to open multiple links at once.

"""

# Generate timestamped results filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
results_filename = f"results_{timestamp}.txt"

domains = []

with open("companies.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        domains.append(line)

with open(results_filename, "w") as out:
    out.write(RESULTS_HEADER)

    for domain in domains:
        out.write(f"{domain}\n")

        for path in CAREER_PATHS:
            query = f'site:{domain} inurl:{path} ' + " ".join(EXCLUSIONS)
            url = GOOGLE_BASE + urllib.parse.quote(query)
            out.write(url + "\n")

        out.write("\n")

print(f"Saved results as {results_filename}")

# Enjoy! Hope this is useful for you. Happy Job Hunting :)

