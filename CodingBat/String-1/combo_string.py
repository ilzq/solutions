"""
String-1 > combo_string
Find this problem at:
https://codingbat.com/prob/p194053

Total completion for String-1 section was just about 12 mins.
Unfortunately it seems like Python is < 3.6 so f-strings cannot be used.
"""


def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a
