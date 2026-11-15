class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {"[":"]","(":")","{":"}"}
        stack = []
        for c in s:
            if c in map_:
                stack.append(map_[c])
            elif not stack or stack.pop() != c:
                return False

        return not stack 
 
        