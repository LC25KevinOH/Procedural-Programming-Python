"""
Handle the output of payroll data in different formats.
"""
import os
import pprint
from datetime import datetime

def give_individual_outputs(which_dict, whic_dir) :
    """
    Function will format and output multiple employee payslips in TXT format.
    """
    now = datetime.now()
    date_str = now.strftime("%m-%Y")

    for ppsn, record in which_dict.items():

        output_name = f"employee_{ppsn}_{date_str}.txt"
        temp_out = os.path.join(whic_dir, "Output", output_name)

        with open(temp_out, "w", encoding="utf-8") as employee_file:
            employee_file.write(f"Payroll Information for Employee PPSN: {ppsn}\n")
            employee_file.write(pprint.pformat(record))
            employee_file.write("\n")

def give_all_output(which_dict, which_dir) :
    """"
    Function will format and store all employees' data into a single CSV output file.
    """
    now = datetime.now()
    date_str = now.strftime("%m-%Y")

    output_data = "PPSN, Name, Gross Salary, Tax Paid, Net Salary\n"
    output_name = f"all_employees_{date_str}.csv"
    output_file_path = os.path.join(which_dir, "Output", output_name)

    for ppsn, record in which_dict.items():
        name = record.get("Name", "Unknown")
        gross_pay = record.get("GrossPay", 0)
        tax = record.get("TaxAmount", 0)
        net_salary = record.get("NetPay", 0)

        output_data += f"{ppsn}, {name}, {gross_pay}, {tax}, {net_salary}\n"

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(output_data)

def what_output(which_dict, which_dir) :
    """
    Function to ask user what output they want.
    1 for individual outputs
    2 for all outputs in one file
    3 for both outputs
    """
    user_input = input(
        "Do you want individual outputs (1), all outputs in one file (2) or both (3)? "
        ).strip().upper()

    if user_input == "1" :
        give_individual_outputs(which_dict, which_dir)
    elif user_input == "2" :
        give_all_output(which_dict, which_dir)
    elif user_input == "3" :
        give_individual_outputs(which_dict, which_dir)
        give_all_output(which_dict, which_dir)
    else :
        print("Invalid input. Please enter '1', '2' or '3'.")
        what_output(which_dict, which_dir)
