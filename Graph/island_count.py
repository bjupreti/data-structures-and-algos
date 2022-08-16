grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

def islandCount(grid):
    if len(grid) == 0: return 0
    visited = set()
    count = 0
    
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if explore(grid, row, col, visited) is True:
                count += 1
    return count
                
                    

def explore(grid, row, col, visited):
    rowInbounds = row >= 0 and row < len(grid)
    columnInbounds = col >= 0 and col < len(grid[0])
    if not rowInbounds or not columnInbounds:
        return False 
    
    if (row, col) in visited: 
        return False
    
    # add in visited set
    visited.add((row, col))
    
    # if water
    if grid[row][col] == 'W': return False
    
    # performing depthFirstSearch
    explore(grid, row - 1, col, visited) # up
    explore(grid, row + 1, col, visited) # down
    explore(grid, row, col - 1, visited) # left
    explore(grid, row, col + 1, visited) # right
    
    return True
            
            
print(islandCount(grid))