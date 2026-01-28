"""
Payroll Processing Application: 
Take input from multiple CSV input files, 
Process/Calculate date and convert into a single output file.
"""
import os
from Functions.read_input import read_csv
from Functions.give_output import what_output
from Functions.calculate_pay import calc_gross, add_bonuses, subtract_tax

#Constants Definition
CURRENT_DIRECTORY = os.path.dirname(__file__)

NAME_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'ppsn_name_payroll_v01.csv')
HOURS_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'hours_worked_payroll_v01.csv')
PAY_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'pay_rate_payroll_v01.csv')
BONUSES_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'bonuses_payroll_v01.csv')
TAX_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'tax_rate_payroll_v01.csv')

def main_function() :
    """
    Main function of program to run other functions
    """
    print("Starting Payroll Processing Application...")

    salary_dict = {}

    read_csv(NAME_FILE_NAME, salary_dict, "Name")
    read_csv(HOURS_FILE_NAME, salary_dict, "Hours")
    read_csv(PAY_FILE_NAME, salary_dict, "Rate")
    read_csv(BONUSES_FILE_NAME, salary_dict, "Bonuses")
    read_csv(TAX_FILE_NAME, salary_dict, "Tax")

    calc_gross(salary_dict)

    add_bonuses(salary_dict)

    subtract_tax(salary_dict)

    what_output(salary_dict, CURRENT_DIRECTORY)

    print("End of Payroll Processing Application...")

if __name__ == "__main__" :
    main_function()
