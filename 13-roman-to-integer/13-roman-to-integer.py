class Solution:
    def romanToInt(self, s: str) -> int:
        d1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        d2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        sum = 0
        for i in d2:
            if i in s:
                sum += int(d2[i])
                s = s.replace(i,'')
        for i in s:
            sum += int(d1[i])
        return sum