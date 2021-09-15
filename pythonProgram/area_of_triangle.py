'''
s = (a+b+c)/2
area = √(s(s-a)*(s-b)*(s-c))
'''

a = 5
b = 6
c = 7

# calculate the semi-perimeter
s = (a+b+c)/2
print('semi-perimeter = ',s)

# calculate area of a triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area) 
print('The area of the triangle is ' ,area) 