from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
    
        for word in strs:
            letters = [0] * 26
            for i, letter in enumerate(word):
                position = ord(letter) - ord("a")
                letters[position] += 1
            result[tuple(letters)].append(word)
        return list(result.values())
            

            
        


 
            

        