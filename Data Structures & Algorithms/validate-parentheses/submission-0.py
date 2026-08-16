class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        open = ['(', '{', '[']

        stack = []

        for ch in s:
            if ch in open:
                stack.append(ch)
            else:
                if not stack or stack.pop() != map[ch]:
                    return False
                    
        return len(stack) == 0