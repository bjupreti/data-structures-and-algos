"""
Write a function canConstruct(target, wordBank) that accepts a target string and an array of strings.

The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array.

You may reuse elements of wordBank as many times as needed.
"""

def canConstruct(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == '': return True
    
    for word in wordBank:
        try:
            indexx = target.index(word) # returns the index if it finds the word else throws ValueError
            if indexx == 0: # if the index is 0 then the word starts with the first letter of target
                suffix = target[len(word):] # slicing the word(current word)
                if canConstruct(suffix, wordBank) is True:
                    memo[target] = True
                    return True
        except ValueError as ve:
            pass
    memo[target] = False
    return False
                
    
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False