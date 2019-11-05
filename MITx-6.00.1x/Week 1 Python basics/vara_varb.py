"""
Exercise: vara varb
Assume that two variables, varA and varB, are assigned values, either numbers
or strings.
Write a piece of Python code that evaluates varA and varB, and then prints out
one of the following messages:
"string involved" if either varA or varB are strings
"bigger" if varA is larger than varB
"equal" if varA is equal to varB
"smaller" if varA is smaller than varB
"""

vara = input("varA = ")
varb = input("varB = ")
if not(vara.isnumeric()) or not (varb.isnumeric()): #.isnumeric() проверяет, все ли символы строки числа. True если да
    print("string involved")
elif vara > varb:
    print("bigger")
elif vara < varb:
    print("smaller")
else:
    print("equal")
