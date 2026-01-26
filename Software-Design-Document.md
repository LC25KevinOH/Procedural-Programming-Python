# Software Design Document : Payroll Processing App

Kevin O' Halloran

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
      - [Payroll Table](#payroll-table)
  - [Testing Approach](#testing-approach)


## Program Overview

This payroll application is a piece software that will assist Users in processing any quantity of Employee data. Users will be able to input multiple files of the CSV format from various Departments and receive processed Output files. This software aims to provide a simple and efficient method for the necessary calculations relating to each Employees Gross and Net pay.  

## Program Requirements

### Functional Requirements

- Read various CSV files to gather data on categories listed in the Input section
- Calculate the each Employees gross pay based on their rate of pay and hours worked
- Add any bonuses (taxable)
- Calculate taxes and Subtract them from total
- Create and Output a table with all calculated data
- Create and Output a payslip for each Employee individually

### Technical Requirements

- Platform: Cross-platform (Windows, Linux, MacOS)
- Language: Developed in Python, ensuring wide support and maintainability
- Database: CSV Files

### Input Format

The input for this program will be in the format of CSV (Comma Separated Values) files. The plan for this program will be to accept various input files, which will be listed below.

#### PPSN / Name

```
PPSN,Name
1234567A,John Smith
```

#### Timetables / Hours Worked

```
PPSN,Hours
1234567A,38
```

#### Pay Rate (Per Hour)

```
PPSN,Rate
1234567A,14
```

#### Bonuses (Taxable)

```
PPSN,Bonuses
1234567A,50
```

#### Tax Rate (Percent/Amount)

```
PPSN,TaxRate
1234567A,25
```

### Output Format

This program will output a single CSV file. The format will be shown below, it will include all relevant information for each employee.

#### Payroll Table

```
PPSN,Name,HoursWorked,GrossPay,Bonuses,TaxPaid,NetPay
1234567A,John Smith,38,532,50,-145,437
```

## Testing Approach

The approach to testing this application will be primarily focused on Unit Testing. This is where each function will be tested with the 'unittest' module to use a specified set of input data to check it will output the expected results.