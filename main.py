import os
from classes import *


### USAGE EXAMPLE ###
if __name__ == '__main__':
    file_directory = 'tests/sample_files'
    files_to_process = os.listdir(file_directory)
    
    for file in files_to_process:
        file_name = file
        file_path = os.path.join(file_directory, file)
        
        try:
            if '$$A2AINP' in file_name:
                df = A2AINP(file_path).convert_to_dataframe()
            if '$$A2AOUT2' in file_name:
                df = A2AOUT2(file_path).convert_to_dataframe()
            if '$$A2PAMB' in file_name:
                df = A2PAMB(file_path).convert_to_dataframe()
            if '$$A2OSUR' in file_name:
                df = A2OSUR(file_path).convert_to_dataframe()
        except:
            print(f"Error processing file: {file_name}")
            continue

    