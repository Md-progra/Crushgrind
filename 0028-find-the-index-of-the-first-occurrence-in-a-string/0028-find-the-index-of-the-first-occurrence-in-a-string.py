class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Understamd: Input is a string
        #Output: An index
        # .find- Find the first occurrence of a substring 
        # return haystack.find(needle)

        # o(n), o(1)
        if not needle:
            return None
        for i in range(len(haystack)- len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
        