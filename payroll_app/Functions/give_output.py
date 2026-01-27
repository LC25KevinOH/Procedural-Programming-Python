"""
Output the salary dictionary in a readable format.
"""
import os
import pprint

def give_output(which_dict, whic_dir) :
    """
    Function will format and store the necessary data into an output file.
    Currently, it just pretty-prints the salary dictionary.
    """
    for ppsn, record in which_dict.items():
        output_name = f"employee_{ppsn}_file.txt"
        
        temp_out = os.path.join(whic_dir, "Output", output_name)

        with open(temp_out, "w", encoding="utf-8") as employee_file:
            employee_file.write(f"Payroll Information for Employee PPSN: {ppsn}\n")
            employee_file.write(pprint.pformat(record))
            employee_file.write("\n")
