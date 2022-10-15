import math
from xml.etree.ElementPath import find

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


#find_dot(grid)finds any empty spots, indicated with '.'
#returns position of that '.'
def find_dot(grid):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == '.':
                #returns location of dot as a tuple
                return (r,c)

    #if there are no dots
    return None

#valid_placement will check number placed is a valid.
#
def valid_placement(grid, num, location):
   #check if in row
    for i in range(len(grid[0])):
        if grid[location[0]][i] == str(num) and location[1] != i:
            return False
    
    #check columns
    for i in range(len(grid)):
        if grid[i][location[1]] == str(num) and location[0] != i:
            return False


   # check subgrids

    # x = int(math.sqrt(len(grid)))
    # beginningSubGrid = r - r % 3
    # endSubGrid = c - c % 3
    # for beginningSubGrid in range(x + beginningSubGrid):
    #     for endSubGrid in range(x + endSubGrid):
    #         if num == grid[beginningSubGrid][endSubGrid]:
    #             return False

    #Returns True if it is a valid number
    #check through each element in a row
    # for i in range(9):
    #     if grid[location[0]][i] == num:
    #         return False

    # #checks each column
    # for j in range(9):
    #     if grid[j][location[1]] == num:
    #         return False
    
    #checks subgrid
    subgridx = location[1] // 3
    subgridy = location[0] // 3

    for x in range(subgridy * 3, subgridy*3 + 3):
        for y in range(subgridx *3, subgridx*3 + 3):
            if grid[x][y] == str(num) and (x,y) != location:
                return False

    return True


def backtracking(grid):

    dots = find_dot(grid)

    if not dots:
        return True
    else:
        row, column = dots
    
    for num in range(1, 10):
        if valid_placement(grid, num, (row, column)) == True:
            grid[row][column] = str(num)

            if backtracking(grid):
                return True

            grid[row][column] = '.'

    return False

if __name__ == "__main__":
    
    sudoku1 = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
    sudoku2 = "...26.7.168..7..9.19...45..82.1...4...46.29...5...3.28..93...74.4..5..367.3.18..."
   
    #turns string into grid
    s = convert(sudoku1)
    printgrid(s)
    backtracking(s)
    printgrid(s)
    
