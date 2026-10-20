class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res


    def decode(self, s: str) -> List[str]:
        res2, i = [] , 0
        
        while i< len(s):
            j = i
            while s[j] != "#":
                j += 1
            else:
                length = int(s[i:j])
                res2.append(s[j+1:j+1+length])
                i = j+1+length
               
            
        return res2

