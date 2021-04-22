# in operator

s1 = "str"
s2 = "string"

# if s1 in s2:
#     print("si in s2")

# for i in s1:
#     if i in s2:
#         print(i)

def rep(str):
    for i in str:
        c = 0
        for j in str:
            if i == j:
                c += 1
                if c > 1:
                    print(i,c)
                else:
                    print("not repeat")

rep("banana")