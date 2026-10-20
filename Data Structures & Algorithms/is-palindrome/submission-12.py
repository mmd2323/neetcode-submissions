class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = "".join(c.lower() for c in s if c.isalpha() or c.isdigit())
        for i in range(len(sentence)):
            j = len(sentence)-1 - i
            if sentence[i] != sentence[j]:
                return False
        return True
            


        