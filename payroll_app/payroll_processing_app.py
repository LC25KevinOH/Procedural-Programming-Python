"""
Payroll Processing Application: 
Take input from multiple CSV input files, 
Process/Calculate date and convert into a single output file.
"""
import os
from Functions.read_input import read_csv
from Functions.give_output import give_output

#Constants Definition
CURRENT_DIRECTORY = os.path.dirname(__file__)

NAME_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'ppsn_name_payroll_v01.csv')
HOURS_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'hours_worked_payroll_v01.csv')
PAY_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'pay_rate_payroll_v01.csv')
BONUSES_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'bonuses_payroll_v01.csv')
TAX_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'tax_rate_payroll_v01.csv')

def calc_gross(which_dict) :
    """
    Calculate each Employees Gross Pay based on Hours Worked and Pay Rate
    (Starts running Total)
    """
    for _, record in which_dict.items():
        hours = record.get("Hours", 0)
        rate = record.get("Rate", 0)
        gross_pay = hours * rate
        record["GrossPay"] = gross_pay

def add_bonuses(which_dict) :
    """
    Simple function to Add Bonuses (parameter)
    (Added to running total before/after Tax)
    """
    for _, record in which_dict.items():
        bonuses = record.get("Bonuses", 0)
        record["GrossPay"] += bonuses

def subtract_tax(which_dict) :
    """
    Calculate the necessary amount of Tax to be Paid based on Tax Rate,
    Subtract from Employee Pay
    (Subtracting from running total)
    """
    for _, record in which_dict.items():
        tax_rate = record.get("Tax", 0)
        tax_amount = (record["GrossPay"] / 100) * tax_rate
        record["TaxAmount"] = tax_amount
        record["NetPay"] = record["GrossPay"] - tax_amount

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
    print("Start..")

    salary_dict = {}

    read_csv(NAME_FILE_NAME, salary_dict, "Name")
    read_csv(HOURS_FILE_NAME, salary_dict, "Hours")
    read_csv(PAY_FILE_NAME, salary_dict, "Rate")
    read_csv(BONUSES_FILE_NAME, salary_dict, "Bonuses")
    read_csv(TAX_FILE_NAME, salary_dict, "Tax")

    calc_gross(salary_dict)

    add_bonuses(salary_dict)

    subtract_tax(salary_dict)

    give_output(salary_dict)

    print("End..")

if __name__ == "__main__" :
    main_function()
