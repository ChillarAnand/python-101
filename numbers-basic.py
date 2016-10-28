#!/usr/bin/python

# example usage:
# $ python numbers-basic.py
# 1 2 3
# Min is:  1
# Max is:  3
# Average is:  2.0

# we can read numbers using input() function
num_string = input()

# the raw_input() function accepts data as strings
# we can split it and map it to ints
nums = list(map(int, num_string.split()))

print("Min is: ", min(nums))
print("Max is: ", max(nums))
print("Average is: ", sum(nums)/len(nums))
