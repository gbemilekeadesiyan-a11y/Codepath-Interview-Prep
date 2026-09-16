"""def validateDigitWindows(numbers):
    n = len(numbers[0])
    result = []

    for c in range(n - 2):
        cells = numbers[0][c:c+3] + numbers[1][c:c+3] + numbers[2][c:c+3]
        result.append(len(set(cells)) == 9)  

    return result  
     
      
       
print(validateDigitWindows([[1,2,3],[4,5,6],[7,8,9]]))   
print(validateDigitWindows([[1,1,1],[1,1,1],[1,1,1]]))  
 """




def runningTotal(amounts):
    result = []    # for a total 
    for a in amounts:
        if not result:
            result.append(a)
        else:
            result.append(result[-1] + a)
    return result


def runningTotal(amounts):
    for i in range(1, len(amounts)):
        amounts[i] += amounts[i - 1]
    return amounts     # just modified amounts... damn  




def validateDigitWindows(numbers):
    n = len(numbers[0])    
    result = [] 
    for c in range(n-2):        # c is the index length of the window? 
        cells = numbers[0][c:c+1] + numbers[0][c:c+2] + numbers[0][c:c+3]     # the cells in the window for every c 
        result.append(len(set(cells)) == 9)
    return result


def isValidGroup(group):
    filled = [x for x in group if x != '.']
    return len(set(filled)) == len(filled) 

def isValidSudoku(grid):
    for r in range(9):
        if not isValidGroup(grid[r]):
            return False

    for c in range(9):
        if not isValidGroup([grid[r][c] for r in range(9)]):
            return False

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            box = grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3]
            if not isValidGroup(box):
                return False

    return True