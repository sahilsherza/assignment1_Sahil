
#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: "Sahil sherzai"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys


def day_of_week(date: str) -> str:

    "Based on the algorithm by Tomohiko Sakamoto"

    day, month, year = (int(x) for x in date.split('/'))

    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}

    if month < 3:

        year -= 1

    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7

    return days[num]

def leap_year(year):

    """

    Returns True if the year is a leap year, False otherwise.

    """

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



def mon_max(month, year):

    """

    Given a month and a year, returns the maximum number of days in that month.

    """

    if month in [1, 3, 5, 7, 8, 10, 12]:

        return 31

    elif month in [4, 6, 9, 11]:

        return 30

    elif month == 2:

        return 29 if leap_year(year) else 28

    else:

        raise ValueError("Invalid month")



def after(date):

    """

    Given a date in YYYY-MM-DD format, returns the next day's date in the same format.

    """

    year, month, day = map(int, date.split('-'))

    day += 1

    if day > mon_max(month, year):

        day = 1

        month += 1

        if month > 12:

            month = 1

            year += 1

    return f'{year:04d}-{month:02d}-{day:02d}'


def day_count(start_date, end_date):

    """

    Counts the number of weekend days (Saturdays and Sundays) between two dates inclusive.

    """

    count = 0

    current_date = start_date

    while current_date <= end_date:

        if day_of_week(current_date) in ["Saturday", "Sunday"]:

            count += 1

        current_date = after(current_date)

    return count

def valid_date(date):

    """

    Validates if the given date is in the YYYY-MM-DD format and is a valid calendar date.

    """

    try:

        year, month, day = map(int, date.split('-'))

        if month < 1 or month > 12:

            return False

        if day < 1 or day > mon_max(month, year):

            return False

        return True

    except ValueError:

        return False

def usage():

    """

    Prints usage message.

    """

    print("Usage: python3 assignment1.py YYYY-MM-DD YYYY-MM-DD")

    exit(1)

if __name__ == "__main__":

    # check length of arguments

    if len(sys.argv) != 3:

        usage()

        

    # check first arg is a valid date

    start_date = sys.argv[1]

    if not valid_date(start_date):

        usage()

        

    # check that second arg is a valid number (+/-)

    num_days = sys.argv[2]

    if not num_days.lstrip('-').isdigit():

        usage()

        

    # call day_iter function to get end date, save to x

    num_days = int(num_days)

    end_date = day_iter(start_date, num_days)

    

    # print(f'The end date is {day_of_week(x)}, {x}.')

    print(f"The end date is {day_of_week(end_date)}, {end_date}.")

    pass
