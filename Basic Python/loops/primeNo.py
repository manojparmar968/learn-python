"""
Write a Python program that checks if a number is prime or not.

If the number is prime, it should print "Prime".

If the number is not prime, it should print "Not prime".

A prime number is only divisible by 1 and by itself. 
It is not the product of two smaller natural numbers.

Note: 0 is neither primer nor composite, 
so the program should print "Not Prime" as the output for the value.

"""

num = 5 # prime number = 2,3,5,7,11

# option 1
# is_Prime = True

# if num == 1:
#     is_Prime = False
# else:
#     for i in range(2, num):
#         if i%2 == 0:
#             is_Prime = False
#             # print("Not Prime")
#             break
#         # else:
#         #     print("Prime")

# if is_Prime:
#     print("Prime")
# else:
#     print("Not Prime")

# option 2

if num == 0 or num == 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
        else:
            print("Prime")
            break

