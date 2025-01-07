from functions import *

import re
import pandas as pd


class RTF_Parse_Base:
    def __init__(self, file_path):
        self.file_path = file_path
        self.rows_per_patient = 3

        self.patient_data_delimiters = {
            'Name': (0, 30),
            'Admit Date': (30, 38),
            'Patient No': (80, 88),
            'MRN': (156, 182),
            'Sex': (182, 183)
        }

        self.string_trunacation_limit = 76

    def convert_to_dataframe(self):
        raw_file = read_raw_file(self.file_path)
        formatted_file = format_file_to_string(raw_file)
        truncated_data = truncate_patient_data(
            formatted_file, self.string_trunacation_limit)
        grouped_items = group_and_concatenate_by_patient(
            self.rows_per_patient, truncated_data)
        grouped_items = remove_duplicates_based_on_prefix(grouped_items)

        patient_data = extract_patient_information(
            self.patient_data_delimiters, grouped_items)

        self.df = pd.DataFrame(patient_data)
        return self.df


class A2AINP(RTF_Parse_Base):
    def __init__(self, file_path):
        super().__init__(file_path)


class A2AOUT2(A2AINP):
    def __init__(self, file_path):
        super().__init__(file_path)

        self.rows_per_patient = 4


class A2PAMB(RTF_Parse_Base):
    def __init__(self, file_path):
        super().__init__(file_path)
        
        
class A2OSUR(RTF_Parse_Base):
    def __init__(self, file_path):
        super().__init__(file_path)
