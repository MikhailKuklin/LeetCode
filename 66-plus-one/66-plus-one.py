class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)
        si= int(s) + 1

        sis = str(si)

        final = []
        for i in sis:
            final.append(int(i))

        return final