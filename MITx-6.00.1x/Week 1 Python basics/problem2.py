"""
Problem 2
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
str = input("Enter test string here: ")
count = 0
str = str.lower()
for i in range(len(str)-2):
    if str[i]=='b' and str[i+1]=='o' and str[i+2]=='b':
        count+=1
print("String contains {0} bob".format(count))