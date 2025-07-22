"""
UnderStand - given a string, and we must remove characters so that no character appears three times in a row.
Match - Sring manipulation;
Plan - Initialize an empty list res = []
for char in s
if  len(res) is greater than/ equal to 2 and res[-1] == res[-2] == char:
    move on to next line without doing nothing (skip it)
Otherwise, append it to res.
return joint list

Implement 
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for char in s:
            if len(res) >= 2 and res[-1] == res[-2] == char:
                continue #doesn't add 
            res.append(char)
        return ''.join(res)





"""
Review -
Evaluate - # Time Complexity is an O(n); where n is the length of a string
#Space Complexity - is an O(n); where  n is the length of the array
"""
        