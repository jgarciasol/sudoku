
'''
Author: Jason Garcia
Description: Sudoku puzzle solver uses AC3 and backtracking to find solution to Sudoku puzzles
It first generates the variables with the generate_boxes function

'''
import queue

'''
This function will generate a box in the grid such as A1, A2 ... 
Returns list 81 boxes
'''
def generate_variables(string1, string2):
    vars = []
    for i in string1:
        for j in string2:
            vars.append(i+j)
    return vars

# COLUMNS = '123456789'
# ROWS = 'abcdefghi'
# NUMS = '123456789' #domain
# variables = generate_variables(ROWS,COLUMNS) #variables

'''
This function makes
A list of all rows [a1, a2, a3 ...]
A list of all columns [a1, a1, a1 ...]
A list of all subgrids [a1, a2, a3, b1, b2, b3, c1, c2, c3]
Returns three lists of all rows, columns, and subgrids
'''
def generate_rows_columns_subgrids(rows,columns):
    all_rows = []
    for r in rows:
        all_rows.append(generate_variables(r, columns))
    #print(all_rows)
    all_columns = []
    for c in columns:
        all_columns.append(generate_variables(rows,c))
    #print(all_columns)
    all_sub_grids = []
    for row_sub_grid in('abc', 'def', 'ghi'):
        for column_sub_grid in ('123','456', '789'):
            all_sub_grids.append(generate_variables(row_sub_grid, column_sub_grid))
    #print(all_sub_grids)
    
    return all_rows, all_columns, all_sub_grids


'''This function takes in an string and assigns each key with a value
    returns a dictionary. If there is no assigned number in a variable, then the possible
    numbers that can go in that variable is a list [1,2,3,4,5,6,7,8,9]
'''
def grid(stringgrid, vars, n):
    domain = []
    nums = n
    for str in stringgrid:
        if str == '.':
            domain.append(nums)
        elif str in nums:
            domain.append(str)
    return dict(zip(vars,domain))


def printboard(dictionary_grid):
    sort_keys = sorted(dictionary_grid)
    for i in range(0,9):
        if i != 0 and i % 3 == 0:
            print("-----------")
        for j in range(0,9):
            if j!= 0 and j % 3 == 0: 
                print("|", end='')
            key = sort_keys[i*9 + j]
            print(dictionary_grid[key], end= '')
        print()

'''Reduce the sudoku board based on the neighbors
    maintaining arc consistency
'''
def remove_inconsistent_vals(grid, neighbors, all_constraints, NUMS):

    removed = False
    numbers = NUMS
    #start doing elimation of domains
    for variable,domain in grid.items():
        if len(domain) != 1: #there needs to be some domains to remove
            keys = neighbors[variable] #get all the variables of neighbors
            final_keys = set([grid[i] for i in keys if len(grid[i]) == 1])
            grid[variable] = ''.join(set(grid[variable]) - final_keys)
            removed = True
   # print(grid)

    #when there is only one possible choice in the domain
    for relations in all_constraints:
        for num in numbers:
            num_placement = [x for x in relations if num in grid[x]]
            if len(num_placement) == 1:
                grid[num_placement[0]] = num

    return removed


def ac3(grid, all_constraints, neighbors, NUMS):
    queue = None
    if queue == None:
        queue = [(xi, xk) for xi in grid.keys() for xk in neighbors[xi]] 
    #print(queue)
    while queue:
        queue.pop()
        if remove_inconsistent_vals(grid, neighbors, all_constraints, NUMS):
            #print(remove_inconsistent_vals(grid, neighbors, all_constraints))
            #return True
            #if there is no possible solution
            if len([variable for variable in grid.keys() if len(grid[variable]) == 0]):
                return False
    return grid

def backtracking(grid):

    ac3_grid = ac3(grid, all_constraints, neighbors, NUMS)
   # AC3 could not remove all domains
    if ac3_grid is False:
       return False

    for var,domain in grid.keys():
        if len(domain) == 1:
            #if ac3_grid is able to solve sudoku
            return ac3_grid

    #pick any variable that has not been solved yet
    var1, x = min((len(ac3_grid[x]), x) for x in variables if len(ac3_grid[x]) > 1)
    
    #print(var1,x)
    #print(x, var1)
    #print(x)
    for n in ac3_grid[x]:
        #copy new grid to attempt finding solution to left over domains
        #new_grid = grid.copy()
        new_grid = dict(list(ac3_grid.items()))
        new_grid[x] = n
        new_grid2 = backtracking(new_grid)
        if new_grid2:
            return new_grid2


if __name__ == "__main__":

    sudoku_string1 = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
    sudoku_string2 = "...26.7.168..7..9.19...45..82.1...4...46.29...5...3.28..93...74.4..5..367.3.18..."
    sudoku_hard = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"

    if len(sudoku_string1) != 81:
        print("Make sure the string is 81 chars long")
    else:
        COLUMNS = '123456789'
        ROWS = 'abcdefghi'
        NUMS = '123456789' #domain
        variables = generate_variables(ROWS,COLUMNS) #variables a1, a2, a3 ... i9 81 variables. 
        #stores the string in a dictionary
        sudoku_dict = grid(sudoku_string1, variables, NUMS)
        #constraints
        all_rows, all_columns, all_subgrids = generate_rows_columns_subgrids(ROWS,COLUMNS)

        # #combines all previous lists to make a list of keys that will represent a sudoku grid
        all_constraints = all_rows + all_columns + all_subgrids
       # print(all_constraints)

        '''
            Each key (i; variables) will have a list of j variables that have relation.
            j is a list of rows, columns, and subgrids
            i = a1: [ [a1, a2, a3 ...], [a1, b1, c1 ...], [a1, a2, a3, b1, b2, b3,],
            i = b2: [[row], [columns], [subgrids]]: 
        '''
        related = {}
        for i in variables:
            temp = []
            #print(len(variables))
            for j in all_constraints:
                if i in j:
                    temp.append(j)
            related[i] = temp
       #print(related)
        #all the neighbors of a variable
        neighbors = {}
        for x in variables:
            #add all lists from related into temp
            temp = sum(related[x],[])
            temp = set(temp)
            #print(type(temp))
            #print(len(temp))

            #remove current variable from set since it cannot be a neighbor of itself
            temp = temp - set([x])
            #print(temp)
            neighbors[x] = temp
        
        #Now we have all of the variables with possible domains, constraints, and neighbors
        sudoku_grid = ac3(sudoku_dict, all_constraints, neighbors, NUMS)
        sudoku_grid = backtracking(sudoku_dict)
        printboard(sudoku_dict)