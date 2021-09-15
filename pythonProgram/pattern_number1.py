"""
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
"""
k=1
i=1
while(i<=5):
    b=1
    while(b<=5-i):
        print(" ",end=" ")
        b=b+1
    j=1
    while(j<=k):
        print(j,end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1
