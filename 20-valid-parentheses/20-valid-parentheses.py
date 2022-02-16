class Solution:
    def isValid(self, s: str) -> bool:
        closed = {')':'(', ']':'[', '}':'{'}
        open = {'(':'(','[':'[', '{':'{'}

        res = []
        for i in s:
            if i in open:
                res.append(i)
            elif res:
                item = res.pop()
                if item != closed[i]: 
                    return False
            else: 
                return False
        
        if not res: 
            return True
        else: 
            return False

