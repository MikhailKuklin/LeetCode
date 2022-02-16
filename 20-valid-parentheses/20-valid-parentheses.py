class Solution:
    def isValid(self, s: str) -> bool:
        hasmap = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        for st in s : 
            if st in ['(', '[', '{'] : 
                stack.append(st)
            elif stack : 
                item = stack.pop()
                if item != hasmap[st]  : 
                    return False
            else : 
                return False
        
        if not stack : 
            return True
        else : 
            return False

