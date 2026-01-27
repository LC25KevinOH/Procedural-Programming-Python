"""
Module to calculate gross and net pay for employees.
"""
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