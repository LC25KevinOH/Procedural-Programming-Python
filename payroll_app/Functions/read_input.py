"""
Read input CSV files and store data in a dictionary.
"""
import csv

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

    if field_name in ["Hours", "Rate", "Bonuses", "Tax"] :
        float_data(dict_to_update, field_name)

def float_data(dict_name, field_name) :
    """
    Convert the specified field in the dictionary to a float.

    Parameters
    ----------
    dict_name : dict
        The dictionary containing the data.
    field_name : str
        The name of the field to convert to float.
    
    Returns
    -------
    None
    """
    for _, record in dict_name.items() :
        record[field_name] = float(record[field_name])
