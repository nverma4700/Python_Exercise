# Convert time 12 hour format to 24 hour format
import math
import os
import random
import re
import sys


def timeConversion(s):
    pattern = r'(\d{2}):(\d{2}):(\d{2})(AM|PM)'
    match = re.match(pattern, s)
    if match:
        hour, minute, second, period = match.groups()
        hour = int(hour)

        if period == 'PM' and hour != 12:
            hour += 12
        elif period == 'AM' and hour == 12:
            hour = 0

        hour = f'{hour:02}'  # Make sure hour is return in 2 digit
        clean_time_str = f'{hour}:{minute}:{second}'

    return clean_time_str


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
