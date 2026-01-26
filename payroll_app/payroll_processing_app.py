"""
Payroll Processing Application: 
Take input from multiple CSV input files, 
Process/Calculate date and convert into a single output file.
"""
import os

CURRENT_DIRECTORY = os.path.dirname(__file__)

INPUT_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'ppsn_name_payroll_v01.csv')
input_list_1 = []

def receive_input() :
    """
    Function will convert data from CSV input files into lists ready for other functions to process.
    """
    first = True

    with open(INPUT_FILE_NAME, "r", encoding="utf-8") as name_storage :
        for line in name_storage :
            if first :
                first = False
            else :
                input_list_1.append(line)
print("Test..")

receive_input()

for item in input_list_1 :
    print(item)
