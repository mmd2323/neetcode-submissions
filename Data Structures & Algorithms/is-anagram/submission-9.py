class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checklist = {}
        checklist2 = {}
        for char in s:
            if char in checklist:
                checklist[char] = checklist[char] + 1
            else:
                checklist[char] = 1
        for char in t:
            if char in checklist2:
                checklist2[char] = checklist2[char] + 1
            else:
                checklist2[char] = 1
        if checklist == checklist2:
            return True
        return False

            
        