"""
String-1 > make_tags
Find this problem at:
https://codingbat.com/prob/p132290
"""


def make_tags(tag, word):
    return '<{0}>{1}</{0}>'.format(tag, word)
