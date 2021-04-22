f = open("abc.txt", "r")
while True:
    line=f.readline()
    elts= line.split()
    try:
        idx=elts[0]
        name=elts[1]
        balance=elts[2]
        print("idx= ",idx)
        print("name = ",name)
        print("balance= ",balance)
    except:
        break
f.close()


# import csv

# # with open('abc.txt', 'r') as csv_file:
# #     csv_reader = csv.reader(csv_file)

# #     for line in csv_reader:
# #         print(line)

# with open("abc.txt", "r") as file:
#     data = file.read()
#     for char in data:
#         print(char)