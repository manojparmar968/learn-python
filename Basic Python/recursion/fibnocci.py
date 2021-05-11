"""
Write a Python program that calculates and prints the nth Fibonacci number.

The value of n represents the position of the element in the sequence.

The initial value of n should be 0.

You may assume that the value of n is a non-negative integer.

The Fibonacci sequence is a series of numbers where the next number is the result of adding the previous two numbers. 
The sequence starts with 0 and 1.

Hints:
Identify the base case and the recursive case.

For the base case: what condition should stop the process?

For the recursive case: how should we continue the process?
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

# option 2

n = 9
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b