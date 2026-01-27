"""
Read input CSV files and store data in a dictionary.
"""
import csv

#Constants Definition
# CURRENT_DIRECTORY = os.path.dirname(__file__)

# NAME_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'ppsn_name_payroll_v01.csv')
# HOURS_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'hours_worked_payroll_v01.csv')
# PAY_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'pay_rate_payroll_v01.csv')
# BONUSES_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'bonuses_payroll_v01.csv')
# TAX_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'tax_rate_payroll_v01.csv')

def read_csv(filename, dict_to_update, field_name) :
    """
    Read a CSV file and update a dictionary with the data found in the file.

    Parameters
    ----------
    filename : str
        The name of the CSV file to read.
    dict_to_update : dict
        The dictionary to update with the data found in the file.
    field_name : str
        The name of the field in the CSV file to use as the key in the dictionary.
    
    Returns
    -------
    None
    """
    with open(filename, encoding="utf-8") as f :
        reader = csv.DictReader(f)
        for row in reader :
            ppsn = row['PPSN']
            field = row[field_name]
            employee_dict = dict_to_update.get(row['PPSN'], {})
            employee_dict[field_name] = field
            dict_to_update[ppsn] = employee_dict

# salary_dict = {}

# read_csv(NAME_FILE_NAME, salary_dict, "Name")
# read_csv(HOURS_FILE_NAME, salary_dict, "Hours")
# read_csv(PAY_FILE_NAME, salary_dict, "Rate")
# read_csv(BONUSES_FILE_NAME, salary_dict, "Bonuses")
# read_csv(TAX_FILE_NAME, salary_dict, "Tax")

# for ppsn, record in salary_dict.items() :
#     record["Hours"] = float(record["Hours"])
#     record["Rate"] = float(record["Rate"])
#     record["Bonuses"] = float(record["Bonuses"])
#     record["Tax"] = float(record["Tax"])
