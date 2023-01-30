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
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle


#!/usr/bin/python3
"""0-pascal_triangle."""

triangle = list()
triangle.append([1])


# def pascal_triangle(n):
#     """
#     Return a list of lists of intergers representing the Pascal's Triangle.

#     temp is temporary list to be storing the elements of to manipulate /
#     to form the new row.
#     row will be every new row of the values of that row position.
#     sumNextValue will be the sum of the values that forms the current row.

#     Args:
#         n (int): The number of rows of the triangle.
#     """
#     if n <= 0:
#         return list()
#     else:
#         for i in range(n - 1):
#             temp = [0] + triangle[-1] + [0]
#             row = list()
#             for j in range(len(triangle[-1]) + 1):
#                 sumNextVal = temp[j] + temp[j + 1]
#                 row.append(sumNextVal)
#             triangle.append(row)
#         return triangle