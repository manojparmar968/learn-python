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

#   option 3 using while loop
nterms = 9

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1, end=" ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

# option 4 using a for loop

a=9
f=0                                         
s=1                                     
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next

# option 5

n = 5

a,b = 0,1
while(a<n):
    print(a,end="")
    a,b = b,a+b
print()