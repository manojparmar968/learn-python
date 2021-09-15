n = 6 # 1*2*3*4*5*6 = 720

fact = 1
for i in range(1, n+1):
    print(i)
    fact *= i
print(fact)