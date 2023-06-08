import urllib.request
import re

# GitHub repository URL
repo_url = "https://github.com/OpenIntroStat/openintro-statistics-learn-obj"

# Directory numbers from 00 to 09
directories = [str(x).zfill(2) for x in range(10)]

# Regular expression pattern to extract learning outcomes
pattern = r"\\item(.*)"

# Iterate over directories and retrieve learning outcomes
learning_outcomes = []
for directory in directories:
    # Construct the URL for the .tex file
    file_url = f"{repo_url}/blob/master/{directory}/{directory}learn_obj.tex"
    raw_file_url = file_url.replace('/blob/', '/raw/')
    
    # Retrieve the file contents
    try:
        with urllib.request.urlopen(raw_file_url) as response:
            content = response.read().decode('utf-8')
        
        # Extract learning outcomes using regular expression
        matches = re.findall(pattern, content)
        
        # Append learning outcomes to the list
        learning_outcomes.extend(matches)
    except urllib.error.HTTPError as e:
        print(f"Failed to retrieve file from URL: {file_url}")
        print(f"HTTP Error {e.code}: {e.reason}")
        print()
        continue

# Print the extracted learning outcomes
for index, outcome in enumerate(learning_outcomes, start=1):
    print(f"Learning Outcome {index}: {outcome.strip()}")