from striprtf.striprtf import rtf_to_text
import re

def read_raw_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def format_file_to_string(rtf_content):
    split_rtf_content = re.split(r'\\line|\\page|\n', rtf_content)
    
    # find the index of the row that has headers in it
    for i, line in enumerate(split_rtf_content):
        # using regex, find the row that has name in it
        if re.search(r'\bNAME\b', line):
            name_index = i
            break
    # remove everything before the line that begins with the word 'NAME'
    split_rtf_content = split_rtf_content[name_index:]
    
    # find the index of the row that has the grand totals in it
    for i, line in enumerate(split_rtf_content):
        if line.startswith('GRAND TOTALS'):
            end_index = i
            break
    split_rtf_content = split_rtf_content[:end_index]
    
    # remove empty lines
    split_rtf_content = [item for item in split_rtf_content if item not in ['', ' ']]
    
    # get only the rows where there are 4 or 5 spaces and then a word
    split_rtf_content_regex = [item for item in split_rtf_content if re.match(r'^\s{4,5}\w', item)]
    
    split_rtf_content_regex = [item for item in split_rtf_content_regex if not re.match(r'^\s{4,5}NAME|^\s{4,5}PT NO|^\s{4,5}MRN|^\s{4,5}PT TYPE', item)]

    return split_rtf_content_regex

def group_and_concatenate_by_patient(num_rows_per_patient, data_list):
    if not data_list:
        return []

    if len(data_list) % num_rows_per_patient != 0:
        raise ValueError(f"Number of rows in the file is not divisible by {num_rows_per_patient}. Please check the file and try again.")
    
    result = []
    for i in range(0, len(data_list), num_rows_per_patient):
        group = data_list[i:i + num_rows_per_patient:]  # Slice to get a group of up to X elements
        concatenated_string = "".join(group) # Concatenate the elements in the group into a string
        result.append(concatenated_string)
    return result

def extract_patient_information(delimiter_dict, grouped_data):
    patients = []
    for row in grouped_data:
        patient_data = {}
        for key, (start, end) in delimiter_dict.items():
            patient_data[key] = row[start:end].strip()
        patients.append(patient_data)
    return patients

def truncate_patient_data(data, truncated_string_length):
    concatenated_data = []
    for row in data:
        data_to_keep = row[:truncated_string_length]
        concatenated_data.append(data_to_keep)
    return concatenated_data

def remove_duplicates_based_on_prefix(strings, prefix_length=38):
    unique_strings = {}
    for string in strings:
        prefix = string[:prefix_length]
        if prefix not in unique_strings:
            unique_strings[prefix] = string
    return list(unique_strings.values())