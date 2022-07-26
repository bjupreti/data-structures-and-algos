"""
Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

The function should return an array containing any combination of elements that add up to exactly the targetSum. 
If there is no combination that adds up to the targetSum, then return null.
"""

def howSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult is not None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return remainderResult
    memo[targetSum] = None  
    return None
    
print(howSum(7, [2,3], {})) # [3,2,2]
print(howSum(7, [5,3,4,7], {})) # [4,3]
print(howSum(7, [2,4], {})) # null
print(howSum(8, [2,3,5], {})) # [2,2,2,2]
print(howSum(300, [7,14], {})) # null