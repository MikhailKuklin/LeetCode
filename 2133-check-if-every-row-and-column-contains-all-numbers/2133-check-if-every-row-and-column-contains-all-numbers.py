class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            l1 = []
            l2 = []
            for j in range(len(matrix)):
                l1.append(matrix[i][j])
                l2.append(matrix[j][i])
                if len(l1) != len(list(set(l1))):
                    return False
                if len(l2) != len(list(set(l2))):
                    return False
        return True