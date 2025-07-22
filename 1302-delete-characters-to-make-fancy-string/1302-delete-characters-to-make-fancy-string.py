"""
UnderStand - given a string, and we must remove characters so that no character appears three times in a row.
Match - Sring manipulation;
Plan - Initialize an empty string res
for char in s
if  len(res) is greater than/ equal to 2 and res[-1] == res[-2] == char:
    move on to next line without doing nothing (skip it)
Otherwise, concatenate to res
return res

Implement 
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        for char in s:
            if len(res) >= 2 and res[-1] == res[-2] == char:
                continue #doesn't add (skips)
            res+=char
        return  res





"""
Review -
Evaluate - # Time Complexity is an O(n); where n is the length of a string
#Space Complexity - Optimized space complexity of O(1)
"""
        