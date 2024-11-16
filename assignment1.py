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

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

# Leap year check

def leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

        return True

    return False



def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...

def after(date_str):

    # Parse the date

    year, month, day = map(int, date_str.split('-'))

    

    # Calculate the next day's date

    day += 1

    if day > mon_max(month, year):  # Adjust for the end of the month

        day = 1

        month += 1

        if month > 12:  # Adjust for the end of the year

            month = 1

            year += 1

    

    return f"{year:04d}-{month:02d}-{day:02d}"




def usage():
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    ...

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    ...
