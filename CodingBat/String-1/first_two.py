"""
String-1 > first_two
Find this problem at:
https://codingbat.com/prob/p184816
"""


def first_two(str):
    if len(str) < 2:
        return str
    return str[:2]
