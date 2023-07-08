import urllib.request
import re

# GitHub repository URL
repo_url = "https://github.com/OpenIntroStat/openintro-statistics-learn-obj"

# Directory numbers from 01 to 09 along with their corresponding chapter names
directories = {
    "01": "Introduction to Data:",
    "02": "Summarizing Data:",
    "03": "Probability:",
    "04": "Distributions of random variables:",
    "05": "Foundations for inference:",
    "06": "Inference for categorical data:",
    "07": "Inference for numerical data:",
    "08": "Introduction to linear regression:",
    "09": "Multiple and logistic regression:"
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
        
        # Exclude specific learning outcomes
        filtered_outcomes = [outcome.strip() for outcome in matches if not (
            outcome.startswith("[") or 
            outcome.startswith("Test yourself:") or 
            outcome.startswith("Reading:") or 
            outcome.startswith("Article:") or 
            outcome.startswith("True/False") or 
            outcome.startswith("True / False") or 
            outcome.startswith("True/ False")
        )]
        
        # Store chapter learning outcomes
        chapter_learning_outcomes[chapter_name] = filtered_outcomes
    except urllib.error.HTTPError as e:
        print(f"Failed to retrieve file from URL: {file_url}")
        print(f"HTTP Error {e.code}: {e.reason}")
        print()
        continue

# Print the extracted learning outcomes by chapter in YAML-like format
for chapter_name, outcomes in chapter_learning_outcomes.items():
    print(f"{chapter_name}")
    print(f"  Topic Outcome:")
    for outcome in outcomes:
        if not (outcome.startswith("Test yourself:") or outcome.startswith("Reading:")):
            print(f"    - {outcome}")
    print()

