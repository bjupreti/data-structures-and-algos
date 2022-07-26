"""
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner.
You may only move down or right.

In how many ways can you travel to the goal on a grid dimensions m * n?

Write a function `gridTraveler(m, n)` that calculate this.
"""
def gridTraveller(m,n, memo = {}):
    key = f"{m},{n}"
    if key in memo:
        return memo[key]
    else:
        if m == 1 and n == 1: return 1
        if m == 0 or n == 0: return 0
        memo[key] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1, memo)
        return memo[key]

print(gridTraveller(0,1)) 
print(gridTraveller(1,1))
print(gridTraveller(2,3))
print(gridTraveller(3,3))
print(gridTraveller(18,18))