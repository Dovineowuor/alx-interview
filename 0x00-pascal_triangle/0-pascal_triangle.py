#!/bin/env python

'''
This function first checks if the input n is less than or equal to 0, and if so, it returns an empty list. 
Otherwise, it initializes a variable triangle with a single list containing the number 1, which represents 
the first row of the triangle. It then uses two nested for loops to generate the remaining rows of the triangle. 
The outer loop iterates n times, starting from 1 and going up to n-1, and the inner loop iterates i times, starting 
from 1 and going up to i-1. The inner loop uses the values from the previous row of the triangle to calculate the 
values of the current row, and appends the resulting value to the current row. After each inner loop, the current 
row is appended to the triangle list. 
Finally, the function returns the triangle list, which contains the full Pascal's triangle.

The first function is the same as the previous solution. The second function print_triangle takes one argument 
triangle that is a list of lists of integers and print the triangle in the format [1] [1,1] [1,2,1] etc.

And in the last if name == "main" block, it will call the print_triangle function and pass the pascal_triangle 
function result as an argument.
'''
def pascal_triangle(n):
    '''
    function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    '''
    triangle = []
    if n <= 0:
        triangle
    else:
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
    return triangle