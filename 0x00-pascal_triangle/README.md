# Pascal's Triangle

The `pascal_triangle` directory contains a Python function that generates Pascal's triangle of a given size `n`.

## Function Signature
```python
def pascal_triangle(n: int) -> List[List[int]]
Input
'n: an integer, where 1 <= n <= 20.'
Output
A list of lists of integers representing the Pascal's triangle of n.
An empty list if n <= 0
Example

    '''>>> pascal_triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]'''

## Note
The function uses the mathematical formula to generate the pascal's triangle, where the element at ith row and jth column is 'C(i, j) = C(i-1, j-1) + C(i-1, j) .'

## Usage
You can import this function in your code and use it to generate Pascal's triangle for any given input.

## Contributing
If you find any bugs or have any suggestions for improvements, please feel free to submit an issue or a pull request.

