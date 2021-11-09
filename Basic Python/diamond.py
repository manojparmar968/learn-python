height = 7
if height % 2 == 0:
    print("Please enter a odd value for height: ")
else:
    middle_row = (height + 2) // 2
    # print(middle_row)
    for i in range(middle_row):
        print(" " * (middle_row-i), "*" * (i*2+1))

    for i in range(middle_row-2,-1,-1):
        print(" "*(middle_row-i), "*" * (i*2+1))
