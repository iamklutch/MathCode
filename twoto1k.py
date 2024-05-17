#!/usr/bin/env python3

num1 = 2 ** 1000
print (num1)
num1 = str(num1)
num2 = 0

for num in num1:
  num2 = num2 + int(num)
print(num2)

