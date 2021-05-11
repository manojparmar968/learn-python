class complex_number:
    def __init__(self,r=0,i=0):
        self.real = r
        self.img = i

    def __str__(self):
        # return ("{0}+{1}i".format(self.real,self.img))
        return f"complex_number = {self.real} + {self.img}i"

    def add_complex(self,obj):
        c3 = complex_number()
        c3.real = self.real + obj.real
        c3.img = self.img + obj.img
        return c3

c1 = complex_number(2,5)
print(c1)
c2 = complex_number(1,4)
print(c2)
c3 = c1.add_complex(c2)
print(c3)


# import re
# pattern = r"[aeiou]"
# string = input()
# if re.search(pattern,string):
#     print("match")
# else:
#     print("not")

