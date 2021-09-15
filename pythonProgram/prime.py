num = 407
if num > 1:
    for i in range(2, num):
        if (num%i) == 0:
            print("{} is not a prime number".format(num))
            print(i,"times",num//i,"is",num)
            break
    else:
        print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))

# option 2 using Flag
numb = 407
flag = False

if numb > 1:
    # check for factors
    for i in range(2, numb):
        if (numb % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(numb, "is not a prime numbber")
else:
    print(numb, "is a prime numbber")
