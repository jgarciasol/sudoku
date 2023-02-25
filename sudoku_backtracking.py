
#This function prints out the grid in the classic Sudoku way
def printgrid(grid):
    print("")
    #iterates through rows
    for r in range(len(grid)):
        #iterates through columns
        for c in range(len(grid)):
            print(grid[r][c], end='')
            if (c + 1) % 3 == 0 and (c+1) % 9 !=0:
                print("|", end='')
        print("")
        if (r+1) % 3 == 0 and (r+1) % 9 !=0:
            print("------------")
    print("")

#This function converts the string into a lists of lists
def convert(s):
    grid = [] #will hold all characters in list
    while s:
        grid.append(s[:9])
        s = s[9:]
    
    grid = list(map(list, grid))
    return grid


# def lists2dict(grid):
#    keys = [l[0] for l in grid]
#    #print(keys)
#    values = [l[1:] for l in grid]
#    #print(values)

#    d = [dict(zip(keys, sub)) for sub in zip(*values)]
#    print(d)

#find_dot(grid)finds any empty spots, indicated with '.'
#returns position of that '.' as a list 
def find_dot(grid):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == '.':
                #returns location of dot as a tuple
                return [r,c]

    #if there are no dots
    return False

#valid_placement will check number placed is a valid. Returns a boolean
def valid_placement(grid, num, r, c):
   #check vertically
    for row in range(len(grid)):
        if grid[row][c] == str(num):
            return False
    
    #check horizontally
    for column in range(len(grid)):
        if grid[r][column] == str(num):
            return False

    #checks subgrids
    grid_row = (r // 3) * 3
    grid_col = (c // 3) * 3
    for r in range(3):
        for c in range(3):
            if grid[grid_row + r][grid_col + r] == str(num):
                return False

    return True

#solves the puzzle using backtracking
def backtracking(grid):

    dots = find_dot(grid)

    if not dots:
        return True
    else:
        row, column = dots[0], dots[1]
    
    for num in range(1, 10):
        if valid_placement(grid, num, row, column) is True:
            grid[row][column] = str(num)

            if backtracking(grid):
                return True

            grid[row][column] = '.'

    return False

if __name__ == "__main__":
    
    sudoku1 = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
    sudoku2 = "...26.7.168..7..9.19...45..82.1...4...46.29...5...3.28..93...74.4..5..367.3.18..."
   
    #turns string into grid
    print("Sudoku string one: ")
    sudoku1 = convert(sudoku1)
    printgrid(sudoku1)
    backtracking(sudoku1) #solves it backtracking
    printgrid(sudoku1)
    #print(sudoku1)
    print("-------------------------------------")
    print("Sudoku string two: ")
    sudoku2 = convert(sudoku2)
    printgrid(sudoku2)
    backtracking(sudoku2)
    printgrid(sudoku2)