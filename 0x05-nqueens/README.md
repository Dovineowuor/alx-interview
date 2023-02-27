# N Queens
This project contains interview coding challenges.

# Setup
```bash
touch 0-nqueens.py
chmod +x 0-nqueens.py
./0-nqueens.py 4

# Lint.
pycodestyle 0-nqueens.py
```

The code above is a Python module for finding solutions to the N queens problem. 
Here's an explanation of the functions declared in the file:

get_input(): This function retrieves and validates the size of the chessboard from the command line argument. 
It checks if the argument is valid and if the chessboard size is at least 4.

is_attacking(pos0, pos1): This function takes two positions on the chessboard and checks if they are 
in an attacking position. It checks if the two positions are in the same row, column, or diagonal.

group_exists(group): This function checks if a group of positions exists in the list of solutions. 
It checks if all the positions in the group are already in a solution.

build_solution(row, group): This function builds a solution for the N queens problem. 
It takes the current row and a group of valid positions and tries to find a solution for the remaining rows.

get_solutions(): This function initializes the list of possible positions on the chessboard and builds 
the solutions for the given chessboard size.

The main function retrieves the chessboard size, gets the solutions and prints them out.