"""
Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.
"""

# def canSum(targetSum, numbers):
#     """
#     canSum iterative approach 
#     """
#     compliments = set()
#     for i in numbers:
#         compliment = targetSum - i # 5 - 3 = 2
#         if compliment in compliments or compliment == 0:
#             return True
#         else:
#             compliments.add(i)
#     return False

def canSum(targetSum, numbers, memo={}):
    """
    canSum recursive approach
    """
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False
    
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) is True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False
    
    

print(canSum(5, [1,2,3,4], {}))
print(canSum(7, [2,4], {}))
print(canSum(5, [5], {}))
print(canSum(300, [7, 14], {}))