'''
The standard form of a quadratic equation is:

ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0

The solutions of this quadratic equation is given by:

(-b ± (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
'''
import cmath
a = 1
b = 5
c = 6

# option 1

eq1 = (-b-(b**2)-(4*a*c)**0.5)/2*a
eq2 = (-b+(b**2)-(4*a*c)**0.5)/2*a
print('The quadratic equation is {} and {}'.format(eq1,eq2))

# option 2

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))