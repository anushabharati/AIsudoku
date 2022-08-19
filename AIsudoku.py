def sudoku_solver(sudoku: np.ndarray):
    
#Main function which returns the solved sudoku in case of a valid sudoku. 
#It returns an array of 9 X 9 with -1 if the sudoku is invalid or not solvable.

    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    
    ### YOUR CODE HERE
    
    if not (check_valid_row_col(sudoku) or check_valid_box(sudoku)):
        return np.ones((9, 9), dtype=int) * -1
    
    cache = dictonaryOfValidValues(sudoku)
    
    if back_Tracking(sudoku, cache):
        return sudoku

    return np.ones((9, 9), dtype=int) * -1

def check_valid_row_col(sudoku : np.ndarray):
    
#The function returns true if the row and column constraints are met for initial input sudoku. 
#It returns false otherwise.

    for x in range(9):

        row = []
        column = []
        for y in range(9):
            row_num = sudoku[x][y]
            
            column_num = sudoku[y][x]
         
            if row_num in row or column_num in column:
                return False

            if row_num != 0:
                row.append(row_num)
                
            if column_num != 0:
                column.append(column_num)

    return True

def check_valid_box(sudoku: np.ndarray):
    
#The function returns true if the box constraint is met for initial input sudoku. It returns false otherwise.    
    
    for row in range(9):
        x = row - row % 3
        for column in range(9):
            y = column - column % 3
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if sudoku[i][j] == sudoku[x][y]:
                        return False
    return True

def find_empty(sudoku: np.ndarray):
    
#The function returns the array i.e. row and column of the next space which is empty, 
#if there is empty space in the sudoku, at the end of the sudoku, it returns None.
    
    empty_space = np.where(sudoku == 0)
    if empty_space:
        empty_space = list(zip(empty_space[0], empty_space[1]))
        if len(empty_space) > 0:
            return empty_space[0]
        else:
            return None
    else:
        return None

def check_valid_number(sudoku : np.ndarray, num: int, place_holder: np.ndarray):

#The function checks for the valid number in the row, column and box.
#If all the constraints are met then returns true otherwise returns false. 
    
    row, column = place_holder
    #Checking row
    for i in range(9):
        if sudoku[place_holder[0]][i] == num and place_holder[1]!= i:
            return False
        
    #Checking column
    for i in range(9):
        if sudoku[i][place_holder[1]] == num and place_holder[0] != i:
            return False
        
    #Checking box
    box_row = place_holder[1] // 3
    box_column = place_holder[0] // 3
    
    for i in range(box_column * 3, box_column * 3 + 3):
        for j in range(box_row * 3, box_row * 3 + 3):
            if sudoku[i][j] == num and (i,j) != place_holder:
                return False
    return True

def back_Tracking(sudoku: np.ndarray, cache):
    
#The function tries to solve the sudoku and returns True if there is a solution 
#otherwise returns False if there is no solution.
    
    search_empty_position = find_empty(sudoku)
    if not search_empty_position:
        return True
    else:
        row, column = search_empty_position

    
    for i in cache[(row, column)]:
        if check_valid_number(sudoku, i, search_empty_position):
            sudoku[row][column] = i

            if back_Tracking(sudoku, cache):
                return True
            sudoku[row][column] = 0
        
    return False

def dictonaryOfValidValues(sudoku: np.ndarray):
    
#The function keeps a dictionary of the empty spaces and returns that dictionary.
#The values are then filled in the backtracking function and the correctValues function.

    cache = dict()
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                cache[(i,j)] = correctValues(sudoku,i,j)
    return cache

def correctValues(sudoku: np.ndarray, row, column):
    
#The function keeps a list of the valid values and returns that list.
#The values are then used in the backtracking function.

    numbers = list()
    
    for number in range(1,10):
        
        value = False
        
        for j in range(9):
            if sudoku[row][j] == number:
                
                value = True
                break
        
        if value  == True:
            continue
        else:
            for i in range(9):
                if sudoku[i][column] == number:
                    value = True
                    break
                    
        if value == True:
            continue
        else:
            rowBox = 3 * (row // 3)
            columnBox = 3 * (column // 3)
            
            for i in range(rowBox, rowBox + 3):
                for j in range(columnBox , columnBox + 3):
                    if sudoku[i][j] == number:
                        value = True
                        break
            
        if value == False:
            numbers.append(number)
    return numbers