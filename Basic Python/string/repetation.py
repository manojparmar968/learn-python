
# Repetation in a string , character should you count

def rep(str):
    for i in str:
        c = 0
        for j in str:
            if i == j:
                c += 1
                if c > 1:
                    print(i,c)
                # else:
                    # print("not repeat")

rep("banana")