class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        check = {}
        check2 = {}
        for ch in s:
            check[ch] = 1 + check.get(ch, 0)

        for ch in t:
            check2[ch] = 1 + check2.get(ch, 0)

        return check == check2
           
        
        

        

