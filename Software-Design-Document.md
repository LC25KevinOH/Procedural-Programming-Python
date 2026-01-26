# Software Design Document

## Program Overview

## Program Requirements

### Functional Requirements

- Read various CSV files to gather data on categories listed in the Input section
- Calculate the each Employees gross pay based on their rate of pay and hours worked
- Add any bonuses (taxable)
- Calculate taxes if necessary and Subtract them from total
- Create and Output a table with all calculated data
- Create and Output a payslip for each Employee individually

### Technical Requirements

- Platform: Cross-platform (Windows, Linux, MacOS)
- Language: Developed in Python, ensuring wide support and maintainability
- Database: CSV Files

### Input Format

The input for this program will be in the format of CSV (Comma Separated Values) files. The plan for this program will be to accept various input files, which will be listed below.

#### PPSN

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
PPSN,TaxRate,Format
1234567A,25,P
```

### Output Format

This program will output a single CSV file. The format will be shown below, it will include all relevant information for each employee.

#### Payroll table

```
PPSN,Name,HoursWorked,GrossPay,Bonuses,TaxPaid,NetPay
1234567A,John Smith,38,532,50,-145,437
```

## Testing Approach