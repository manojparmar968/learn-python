"""
                    PROBLEM DESCRIPTION

Charles is in his last year of engineering collage and is still scared of maths, so he passed on his
assignment to you.

He believes that any integer of the form A^x + B^y makes him angry. So, he gives you an integer
array X of size N.

For each X[i], You have to find count of angry integer less than X[i].

                    INPUT FORMAT:
The first line of input contains an integer N which denotes the size of array.

The second line of input contains an integer A.

The third line of input contains an integer B.

The fourth line of input contains an integer array X of size N.

                    Output Format:
For each X[i] output the count of angry integer less than X[i] on a new line.

                    Sample Input:
3
10
3

2 4 11 

                    Sample Output:
0
1
3

                    Constraints:
1 <=N <= 100000
1 <=A,B <= 1000
1 <= X[i] < 2^(31)
0<=0 x,y
"""