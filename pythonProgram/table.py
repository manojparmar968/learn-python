table = int(input("enter a table number: "))
for i in range(1,table+1):
    print("  ")
    print("table number of: ",i)
    print("  ")
    for j in range(1, 11):
        print(i,"*",j," = ",i*j)
    