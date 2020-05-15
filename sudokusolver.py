class HyperSudoku:
    @staticmethod
    def solve(grid):
        """
        Input: An 9x9 hyper-sudoku grid with numbers [0-9].
                0 means the spot has no number assigned.
                grid is a 2-Dimensional array. Look at
                Test.py to see how it's initialized.

        Output: A solution to the game (if one exists),
                in the same format. None of the initial
                numbers in the grid can be changed.
                'None' otherwise.
        """
        # recursively backtrack all possible values until a solution found.
        first_null_element = HyperSudoku.full_grid(grid)
        if first_null_element == None:
            return grid
        i = first_null_element[0]
        j = first_null_element[1]
        for n in range(1, 10):
            if n not in grid[i]:
                for row in range(9):
                    unique = True
                    if grid[row][j] == n:
                        unique = False
                        break
                # check if a duplicate exists in the column
                if unique:
                    # check if it is unique value in square starting from
                    # row at i // 3 and starting col at j // 3
                    if HyperSudoku.square_check(grid, i - i % 3, j - j % 3, n):
                        # then check if it is unique value in hypersquare
                        # by square_check(grid, row_start, column_start, value)
                        # if position is not in any hypersquare
                        (row, col) = (i, j)
                        hyper =  False
                        if (i >= 1 and i <= 3) and (j >= 1 and j <= 3):
                            # (upper left hypersquare
                            (row, col, hyper) = (1, 1, True)
                        elif (i >= 1 and i <= 3) and (j >= 5 and j <= 7):
                            # (upper  right hypersquare)
                            (row, col, hyper) = (1, 5,  True)
                        elif (i >= 5 and i <= 7) and (j >= 1 and j <= 3):
                            # (bottom left hypersquare)
                            (row, col, hyper) = (5, 1,  True)
                        elif (i >= 5 and i <= 7) and (j >= 5 and j <= 7):
                            # (bottom right hypersquare)
                            (row, col, hyper) = (5, 5, True)
                        # add n to position iff it (having passed row, col and square rule  by now)
                        # we are not in a hypersquare or we are in a hypersquare
                        # and n follows the hypersquare rule
                        if (not hyper) or (hyper and HyperSudoku.square_check(grid, row, col, n)):
                            grid[i][j] = n
                            # check if the rest of the grid is solvable and return if so
                            if HyperSudoku.solve(grid):
                                return HyperSudoku.solve(grid)
                            # otherwise, retry
                            grid[i][j] = 0
        return None     # Update this to return correctly
    @staticmethod
    def printGrid(grid):
        """
        Prints out the grid in a nice format. Feel free
        to change this if you need to, it will NOT be 
        used in marking. It is just to help you debug.

        Use as:     HyperSudoku.printGrid(grid)
        """
        print("-"*25)
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(grid[i][j], end=" ")
                if (j % 3 == 2):
                    print("|", end=" ")
            print()
            if (i % 3 == 2):
                print("-"*25)

    @staticmethod
    def full_grid(grid):
        """
        returns the index of the first (right down) empty element found.
        returns None otherwise.
        """
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return [i, j]
        return None
    @staticmethod
    def square_check(grid, r_start, c_start, n):
        """
        checks if n exists in any the 3x3 square
        of the grid given its row start and column start
        """
        for i in range(3):
            for j in range(3):
                if (grid[i + r_start][j + c_start] == n):
                    return False
        return True
