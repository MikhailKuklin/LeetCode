class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s:
            return True
        elif 'b' not in s:
            return True
        else:
            #an = s.count("a")
            #bn = s.count("b")
            if len(s) == 2:
                if s[0] == 'a':
                    return True
            else:
                l = []
                for i in range(0, len(s)):
                    try:
                        if s[i] == 'b':
                            if s[i+1] == 'a':
                                l.append(False)
                        elif s[i] == 'a':
                            if s[i+1] == 'a' or s[i+1] == 'b':
                                l.append(True)
                            elif s[i-1] == 'b':
                                l.append(False)
                    except IndexError:
                        break
                if all(l) == True:
                    return True
                else:
                    return False