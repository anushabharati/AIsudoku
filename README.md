# AIsudoku
This is a sudoku solver using AI algorithms

Sudoku Solver

Given Problem

A given 9X9 sudoku:
    The **X** is set of Variables are reprensented in a 9 X 9 - 2D array.
    The **D** is domain of the variables is from 1 to 9.
    There are certain **C** constraints given by:
* Each cells can contain only one single value.
* The input sudoku cannot be altered in any form.
* Each row of the sudoku can contain numbers from 1 to 9 once only, no duplicates are allowed. 
* Each column of the sudoku can contain numbers from 1 to 9 once only, no duplicates are allowed. 
* Each square of the size 3 X 3 can contain numbers from 1 to 9 once only, no duplicate are allowed.

Choice of Algorithms

After considering the problem statement, the solution that comes to mind is to classify the problem statement as constraint satisfaction problem. I have implemented the functions in my code to satisfy the constraints C described above. The assignment to the values are done in such a way that no constraints are violated, making sure every variable reaches a state with complete assignment and are consistent. The states with partial assignment should also satisfy the constraints and be consistent.

All this resulted into implementing the depth first search algorithm along with the Constraint satisfaction and backtracking algorithm

The following algorithms are implemented by me:

#BACKTRACKING ALGORITHM:

I implemented the backtracking algorithm because it has a good performance with some exceptions for the hard sudokus as they contain more empty squares than the easier ones. This increases the time complexity of the code as the empty squares have to be filled with increased recursion. The backtracking algorithm tries the brute force method i.e. it tries all the solutions to the problem before choosing the solution which is best.[3] The algorithm tries to find the solution step by step increasing the levels and using the recursion until the correct solution is reached. It uses the Depth-first-search method to implement this logic. Depth-first-search method works like - the algorithm tries to search for a complete assignment via recursion and when a dead node is reached on a branch then we backtrack and try a different solution(number) until we reach a complete assignment which is consistent. If there is no solution or the input is invalid, to the given sudoku then we return the output with 9 X 9 array having -1. 

#CHECKING INPUT SUDOKU VALIDITY

I have implemented a functionality that validates if the input sudoku provided is valid. If the input is valid then the function returns true and the backtracking function is called to solve the sudoku. Otherwise if the input sudoku is invalid then the output sudoku will have -1 in all the places. This is just a check to do before sending the sudoku to the backtracking algorithm.

#IMPLEMENTING THE CACHE

To reduce the time taken by the algorithm to find the empty spaces in the sudoku to fill them. I have created a dictionary of all the cells not filled. After that I created a list of all values for each cell that can be filled in the empty spaces. This created a index of numbers which can be used rather than searching for the empty spaces again and again, reducing the run time by approx. 40 secs on the hard sudokus.

Attempts and Results:

ATTEMPTS

My first attempt at using the algorithms such as depth first search, constraint satisfaction and backtracking algorithm led to all the sudokus solved but the hard sudokus took over 20seconds (about 111 seconds).

This led me to do my research in understanding how to optimize the code and try to reduce the time. I tried to optimize my code by reducing the looping, removing unnecessary codes and using dictionary and list to store the prefetched values. Thus reducing the time for hard sudokus down to 48 seconds. 
Further research led me to different algorithms, such as the rule based algorithm or the Algorithm X combined with dancing links. These could reduce the time of the hard sudokus down to milliseconds.[1]

RESULTS:

The code can solve most of the sudokus under 20 secs except a few hard sudokus, which take time due to the high complexity. Giving a solution for them requires a different algorithm like the rule based algorithm or the Algorithm X combined with dancing links.[2]

Function list

1. sudoku_solver(sudoku: np.ndarray):
This is the main function which returns the solved sudoku in case of a valid sudoku. It returns an array of 9 X 9 with -1 if the sudoku is invalid or not solvable.

2. check_valid_row_col(sudoku : np.ndarray):
The function returns true if the row and column constraints are met for initial input sudoku. It returns false otherwise.

3. check_valid_box(sudoku: np.ndarray):
The function returns true if the box constraint is met for initial input sudoku. It returns false otherwise.

4. find_empty(sudoku : np.ndarray):
The function returns the array i.e. row and column of the next space which is empty, if there is empty space in the sudoku, at the end of the sudoku, it returns None. 

5. check_valid_number(sudoku : np.ndarray, num: int, place_holder: np.ndarray):
The function checks for the valid number in the row, column and box. If all the constraints are met then returns true otherwise returns false. 

6. back_Tracking(sudoku: np.ndarray, cache):
The function tries to solve the sudoku and returns True if there is a solution otherwise returns False if there is no solution.

7. dictonaryOfValidValues(sudoku: np.ndarray):
The function keeps a dictionary of the empty spaces and returns that dictionary. The values are then filled in the backtracking function and the correctValues function.

8. correctValues(sudoku: np.ndarray, row, column):
The function keeps a list of the valid values and returns that list. The values are then used in the backtracking function.

References:
1. Algorithm X in 30 lines![online] Available from: https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html [Accessed 27 March 2022]
2. Sudoku Solver in Python[online] Available from : https://liorsinai.github.io/coding/2020/07/27/sudoku-solver.html [Accessed 27 March 2022]
3. A study of Sudoku solving algorithms [online] Available from: https://www.csc.kth.se/utbildning/kth/kurser/DD143X/dkand12/Group6Alexander/final/Patrik_Berggren_David_Nilsson.report.pdf [Accessed 26 March 2022]
