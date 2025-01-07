from classes import *
import os
from pathlib import Path

cwd = os.getcwd()
print(cwd)

def test_A2AINP_files():
    file_path = Path(cwd) / 'tests' / 'sample_files' / '01062025_$$A2AINP.rtf'
    df = A2AINP(file_path).convert_to_dataframe()
    assert df.shape == (31, 5)

def test_A2AOUT2_files():
    file_path = Path(cwd) / 'tests' / 'sample_files' / '01062025_$$A2OUT2.rtf'
    df = A2AOUT2(file_path).convert_to_dataframe()
    assert df.shape == (504, 5)
    
def test_A2PAMB_files():
    file_path = Path(cwd) / 'tests' / 'sample_files' / '01062025_$$A2PAMB.rtf'
    df = A2PAMB(file_path).convert_to_dataframe()
    assert df.shape == (312, 5)

def test_A2OSUR_files():
    file_path = Path(cwd) / 'tests' / 'sample_files' / '12232024_$$A2OSUR.rtf'
    df = A2OSUR(file_path).convert_to_dataframe()
    assert df.shape == (4, 5)