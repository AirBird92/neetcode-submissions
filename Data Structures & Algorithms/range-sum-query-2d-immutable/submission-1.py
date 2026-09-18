class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row_prefix = []
        for row in matrix:
            prefix = []
            total = 0
            for i in range(len(row)):
                prefix.append(total)
                total += row[i]
            prefix.append(total)
            self.row_prefix.append(prefix)
        print(self.row_prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            total += self.row_prefix[r][col2 + 1] - self.row_prefix[r][col1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)