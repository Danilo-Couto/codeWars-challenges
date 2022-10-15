# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example
s = '12:45:54PM'
# Return '12:01:00'.

# s = '12:40:22AM'
# Return '00:01:00'.

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
# timeConversion has the following parameter(s):


def timeConversion(s):
    last_2_char = s[-2:]
    if last_2_char == 'PM':
        if s[:2] == '12':
            return s[:-2]
        else:
            hour_converted = str(12 + int(s[:2]))
            new_s = s.replace(s[:2], hour_converted)
            return new_s[:-2]
    else:
        if s[:2] == '12':
            new_s = s.replace(s[:2], '00')
            return new_s[:-2]
        else:
            return s[:-2]


print(timeConversion(s))