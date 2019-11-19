"""
Problem 3
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur
in alphabetical order. For example, if s = 'azcbobobegghakl', then your program
should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print
Longest substring in alphabetical order is: abc
"""
str = input("Enter test string here: ")
length = 1
index = 0
maxlength = 1
maxindex = 0
for i in range(len(str) - 1):
    if str[i] <= str[i + 1]:
        length = length + 1
    else:
        if length > maxlength:
            maxlength = length
            maxindex = index
        index = i + 1
        length = 1
if length > maxlength:
    maxlength = length
    maxindex = index
print("Longest substring in alphabetical order is: {}".format(str[maxindex:maxindex + maxlength]))
