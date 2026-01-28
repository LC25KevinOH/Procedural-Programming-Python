"""
Output the salary dictionary in a readable format.
"""
import os
import pprint

def give_individual_outputs(which_dict, whic_dir) :
    """
    Function will format and output multiple employee payslips in TXT format.
    """
    for ppsn, record in which_dict.items():
        output_name = f"employee_{ppsn}_file.txt"

        temp_out = os.path.join(whic_dir, "Output", output_name)

        with open(temp_out, "w", encoding="utf-8") as employee_file:
            employee_file.write(f"Payroll Information for Employee PPSN: {ppsn}\n")
            employee_file.write(pprint.pformat(record))
            employee_file.write("\n")

def give_all_output(which_dict, which_dir) :
    """"
    Function will format and store all employees' data into a single CSV output file.
    """
    output_data = "PPSN, Name, Gross Salary, Tax Paid, Net Salary\n"
    output_file_path = os.path.join(which_dir, "Output", "all_employees_output.csv")

    for ppsn, record in which_dict.items():
        name = record.get("Name", "Unknown")
        gross_pay = record.get("GrossPay", 0)
        tax = record.get("TaxAmount", 0)
        net_salary = record.get("NetPay", 0)

        output_data += f"{ppsn}, {name}, {gross_pay}, {tax}, {net_salary}\n"

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(output_data)
