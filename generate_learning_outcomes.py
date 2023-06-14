import urllib.request
import re

# GitHub repository URL
repo_url = "https://github.com/OpenIntroStat/openintro-statistics-learn-obj"

# Directory numbers from 00 to 09 along with their corresponding chapter names
directories = {
    "00": "OpenIntro: Statistics",
    "01": "Chapter 1: Introduction to Data",
    "02": "Chapter 2: Summarizing Data",
    "03": "Chapter 3: Probability",
    "04": "Chapter 4: Distributions of random variables",
    "05": "Chapter 5: Foundations for inference",
    "06": "Chapter 6: Inference for categorical data",
    "07": "Chapter 7: Inference for numerical data",
    "08": "Chapter 8: Introduction to linear regression",
    "09": "Chapter 9: Multiple and logistic regression"
}

# Regular expression pattern to extract learning outcomes
pattern = r"\\item(.*)"

# Iterate over directories and retrieve learning outcomes
chapter_learning_outcomes = {}
for directory, chapter_name in directories.items():
    # Construct the URL for the .tex file
    file_url = f"{repo_url}/blob/master/{directory}/{directory}learn_obj.tex"
    raw_file_url = file_url.replace('/blob/', '/raw/')
    
    # Retrieve the file contents
    try:
        with urllib.request.urlopen(raw_file_url) as response:
            content = response.read().decode('utf-8')
        
        # Extract learning outcomes using regular expression
        matches = re.findall(pattern, content)
        
        # Store chapter learning outcomes
        chapter_learning_outcomes[chapter_name] = matches
    except urllib.error.HTTPError as e:
        print(f"Failed to retrieve file from URL: {file_url}")
        print(f"HTTP Error {e.code}: {e.reason}")
        print()
        continue

# Print the extracted learning outcomes by chapter
for chapter_name, outcomes in chapter_learning_outcomes.items():
    print(chapter_name)
    print("-" * len(chapter_name))
    for index, outcome in enumerate(outcomes, start=1):
        print(f"- {outcome.strip()}")
    print()
