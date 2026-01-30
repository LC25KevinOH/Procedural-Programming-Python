# Software Design Document : Payroll Processing App

Author: Kevin O' Halloran

- [Software Design Document : Payroll Processing App](#software-design-document--payroll-processing-app)
  - [Program Overview](#program-overview)
  - [Program Requirements](#program-requirements)
    - [Functional Requirements](#functional-requirements)
    - [Technical Requirements](#technical-requirements)
    - [Input Format](#input-format)
      - [PPSN / Name](#ppsn--name)
      - [Timetables / Hours Worked](#timetables--hours-worked)
      - [Pay Rate (Per Hour)](#pay-rate-per-hour)
      - [Bonuses (Taxable)](#bonuses-taxable)
      - [Tax Rate (Percent / Amount)](#tax-rate-percentamount)
    - [Output Format](#output-format)
      - [CSV Output](#csv-output)
      - [TXT Output](#txt-output)
  - [Testing Approach](#testing-approach)


## Program Overview

This payroll application is a piece software that will assist Users in processing any quantity of Employee data. Users will be able to input multiple files of the CSV format from various Departments and receive processed Output files. This software aims to provide a simple and efficient method for the necessary calculations relating to each Employees Gross and Net pay.  

## Program Requirements

### Functional Requirements

- Read various CSV files to gather data on categories listed in the Input section
- Calculate the each Employees gross pay based on their rate of pay and hours worked
- Add any bonuses (taxable)
- Calculate taxes and Subtract them from total
- Create and Output a table with all calculated data (CSV Format)
- Create and Output a payslip for each Employee individually (TXT Format)

### Technical Requirements

- Platform: Cross-platform (Windows, Linux, MacOS)
- Language: Developed in Python, ensuring wide support and maintainability
- Database: CSV Files

### Input Format

The input for this program will be in the format of CSV (Comma Separated Values) files. The plan for this program will be to accept 5 input files, which will be listed below.

#### PPSN / Name
Filename: 'ppsn_name_payroll_v01.csv'

Example:
```
PPSN,Name
1234567A,John Smith
```

#### Timetables / Hours Worked
Filename: 'hours_worked_payroll_v01.csv'

Example:
```
PPSN,Hours
1234567A,38
```

#### Pay Rate (Per Hour)
Filename: 'pay_rate_payroll_v01.csv'

Example:
```
PPSN,Rate
1234567A,14
```

#### Bonuses (Taxable)
Filename: 'bonuses_payroll_v01.csv'

Example:
```
PPSN,Bonuses
1234567A,50
```

#### Tax Rate (Percent/Amount)
Filename: 'tax_rate_payroll_v01.csv'

Example:
```
PPSN,TaxRate
1234567A,20
```

### Output Format

This program will output either a single CSV file or multiple TXT files depending on User choice. The format will be shown for both below. The CSV will provide information for all Employees, while each TXT payslips will provide for a specific Employee.

#### CSV Output
Filename: 'all_employees_{month}-{year}.csv'

Example:
```
PPSN,Name,Gross Salary,Tax Paid,Net Salary
1234567A, John Smith, 582.0, 116.4, 465.6
```

#### TXT Output
Filename: 'employee_{ppsn}_{month}-{year}.txt'

Example:
```
========================================
Payroll Information
Employee PPSN: 1234567A
Name: John Smith
Pay Date: 01-2026
----------------------------------------
Gross Pay:                   582.00
Tax Paid:                    116.40
Net Pay:                     465.60
========================================
```

## Testing Approach

The approach to testing this application would be primarily focused on Unit Testing. This is where each function will be tested with the 'unittest' module to use a specified set of input data to check it will output the expected results.

This program will instead have a more basic approach to testing based on the size/scope of the functionality. There will be 5 main basic tests manually performed to check different levels of functionality. They will be listed here, but for a more detailed description can be found in the 'Procedural Programming – Report Document' file.

Testing:
 - To run the program and check for any errors
 - To check if the program can read the given input files and produce the desired output files 
 - To check the output files for expected result based on a given input 
 - To check if the app meets compatible criteria for potentially running on Linux
 - To test User input section of the program to see: 1. each valid option 2. an invalid option