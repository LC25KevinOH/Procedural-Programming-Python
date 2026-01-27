"""
Payroll Processing Application: 
Take input from multiple CSV input files, 
Process/Calculate date and convert into a single output file.
"""
import os
from Functions.read_input import read_csv

#Constants Definition
CURRENT_DIRECTORY = os.path.dirname(__file__)

NAME_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'ppsn_name_payroll_v01.csv')
HOURS_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'hours_worked_payroll_v01.csv')
PAY_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'pay_rate_payroll_v01.csv')
BONUSES_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'bonuses_payroll_v01.csv')
TAX_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'tax_rate_payroll_v01.csv')

def calc_gross() :
    """
    Calculate each Employees Gross Pay based on Hours Worked and Pay Rate
    (Starts running Total)
    """

def add_bonuses() :
    """
    Simple function to Add Bonuses (parameter)
    (Added to running total before/after Tax)
    """

def subtract_tax() :
    """
    Calculate the necessary amount of Tax to be Paid based on Tax Rate,
    Subtract from Employee Pay
    (Subtracting from running total)
    """

# def give_output() :
#     """
#     Function will format and store the necessary data into an output file.
#     """
#     for employee in EMPLOYEE_LIST :
#         temp = employee.strip().split(",")
#         output_name = "employee_" + temp[0] + "_file.txt"

#         temp_out = os.path.join(CURRENT_DIRECTORY, output_name)

#         with open(temp_out, "x", encoding="utf-8") as employee_file:
#             employee_file.write(f"Your name is: {temp[1]}")

def main_function() :
    """
    Main function of program to run other functions
    """
    print("Test..")

    salary_dict = {}

    read_csv(NAME_FILE_NAME, salary_dict, "Name")
    read_csv(HOURS_FILE_NAME, salary_dict, "Hours")
    read_csv(PAY_FILE_NAME, salary_dict, "Rate")
    read_csv(BONUSES_FILE_NAME, salary_dict, "Bonuses")
    read_csv(TAX_FILE_NAME, salary_dict, "Tax")

    print(salary_dict)

if __name__ == "__main__" :
    main_function()
