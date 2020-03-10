# -*- coding: utf-8 -*-
"""
What's Your Name?


You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last name ≤ .

Output Format

Print the output as mentioned above.

"""

def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." %(a, b))
#	print "Hello {0} {1}! You just delved into python.".format(raw_input(), raw_input())
#   print("Hello {} {}! You just delved into python.".format(first_name,last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

