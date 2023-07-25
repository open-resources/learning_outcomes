# Author: Firas Moosvi
# Date: 2021-05-09

"""Processes all questions.

Usage: 
    process_outcomes.py <file>
"""

from docopt import docopt

## Imports

# Loading and Saving files & others
import pathlib
import yaml
import pandas as pd
import pathlib

def main():

    files = list(pathlib.Path().glob('*.yml'))

    for file in files:

        # Read file
        mdtext = pathlib.Path(file).read_text()
        
        # Parse as YAML
        outcomes = yaml.safe_load(mdtext)
        
        topic_counter = 1
        rows = []

        for k1,v1 in outcomes.items():

            subtopic_counter = 1
            subsubtopic_counter = 1

            for k2,v2 in v1.items():
                subsubtopic_counter = 1
                try:
                    for k3,v3 in v2.items():
                        for i,lo in enumerate(v3):
                            rows.append([k1,k2,k3,lo,f"{topic_counter}.{subtopic_counter}.{subsubtopic_counter}.{i}" ])
                            #print(k1+','+k2+',',k3,',',v,',','{0}.{1}.{2}.{3}'.format(topic_counter,subtopic_counter,subsubtopic_counter,i))
                        subsubtopic_counter += 1
                except AttributeError:
                    for i,lo in enumerate(v2):
                        rows.append([k1,k2,'',lo,f"{topic_counter}.{subtopic_counter}.{subsubtopic_counter}.{i}" ])
                        #print(k1+','+k2+',','',',',v,',','{0}.{1}.{2}.{3}'.format(topic_counter,subtopic_counter,subsubtopic_counter,i))
                subtopic_counter += 1
            topic_counter += 1
            
        export_path = 'outputs_csv' / file.relative_to('.').with_suffix('.csv')

        pd.DataFrame.from_records(rows,columns=['Topic','Subtopic','Subsubtopic','Learning Outcome','Code']).to_csv(export_path,index=None)
    
if __name__ == '__main__':
    main()