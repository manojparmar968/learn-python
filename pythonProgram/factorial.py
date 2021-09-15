# For example, the factorial of 6 is 1*2*3*4*5*6 = 720

num = 7
fact = 1

if num < 0:
    print("Factoril is Not exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print("fact", fact)