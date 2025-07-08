class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pairs = {'()','[]', '{}'}

        for character in s:
            if character in '([{':
                stack.append(character)
            elif not stack or stack.pop()+ character not in valid_pairs:
                return False

        return not stack
        