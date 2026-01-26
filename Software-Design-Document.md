# Software Design Document

## Program Overview

## Program Requirements

### Functional Requirements

### Technical Requirements

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