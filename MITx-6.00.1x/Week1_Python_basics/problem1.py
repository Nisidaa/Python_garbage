"""
Problem 1
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if
s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""
vowels = ['a', 'e', 'i', 'u', 'o', 'A', 'E', 'I', 'U', '']
str = input("Enter test string here: ")
count = 0
for char in str:
    if char in vowels:
        count += 1
print("String contains {0} vowels".format(count))
