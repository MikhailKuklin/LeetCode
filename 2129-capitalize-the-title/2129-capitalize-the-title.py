class Solution:
    def capitalizeTitle(self, title: str) -> str:
        n = title.lower()
        nl = n.split(' ')

        fs = ""
        for i in nl:
            if not fs and len(i) <= 2:
                fs += i
            elif not fs and len(i) > 2:
                fs += i.capitalize()
            elif len(i) <= 2:
                fs += ' '
                fs += i
            else:
                fs += ' '
                fs += i.capitalize()

        return fs