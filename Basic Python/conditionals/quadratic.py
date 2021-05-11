"""
Write a Python program that prints the positive and negative solutions (roots) for a quadratic equation.

If the equation only has one solution, print the solution as the output.

If it has two solutions, print the negative one first and the positive one second on the same line.

If the equation has no real solutions, print "Complex Roots".

You can determine the number of solutions with the discriminant (the result of b^2 - 4ac in the formula below).

- If it's negative, the equation has no real solutions (only complex roots).

- If it's 0, there is only one solution.

- If it's positive, there are two real solutions.

Hints:
a, b, and c should be variables in the program.

You might want to find the value of the discriminant first to determine the number of solutions.

Notice that there is a +- symbol in the formula. In code, you may implement this as two different expressions that return different values.

The math module can be helpful to implement this solution. You can import it with import math and then call its functions with this syntax math.<function>(<args>).
"""
