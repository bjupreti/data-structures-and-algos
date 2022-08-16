grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

def minimum_island(grid):
    visited = set()
    min = float('inf')
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            count = explore(grid, row, col, visited)
            if count != 0 and count < min:
                min = count
    return min

def explore(grid, row, col, visited):
    rowInbounds = row >= 0 and row < len(grid)
    colInbounds = col >= 0 and col < len(grid[0])
    
    if not rowInbounds or not colInbounds:
        return 0
    
    if (row, col) in visited:
        return 0
    
    visited.add((row, col))
    
    if grid[row][col] == 'W':
        return 0
    
    size = 1
    
    size += explore(grid, row - 1, col, visited) + \
        explore(grid, row + 1, col, visited) + \
        explore(grid, row, col - 1, visited) + \
        explore(grid, row, col + 1, visited)
    return size


print(minimum_island(grid))