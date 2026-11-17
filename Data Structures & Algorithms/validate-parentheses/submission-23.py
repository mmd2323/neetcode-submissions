class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"{":"}", "[":"]" , "(": ")" }
        for c in s:
            if c in map:
                stack.append(map[c])
            elif not stack or c != stack.pop():
                return False
        return stack == []

        