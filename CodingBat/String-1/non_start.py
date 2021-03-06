"""
String-1 > non_start
Find this problem at:
https://codingbat.com/prob/p127703
"""


def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a
