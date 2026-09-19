class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [[False] * 9 for _ in range(9)]
        col_set = [[False] * 9 for _ in range(9)]
        box_set = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                s = board[i][j]
                if s == ".":
                    continue
                
                val = int(s) - 1
                if row_set[i][val] or col_set[j][val] or box_set[i // 3][j // 3][val]:
                    return False
                row_set[i][val] = True
                col_set[j][val] = True
                box_set[i // 3][j // 3][val] = True
        return True