class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        square = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e == '.':
                    continue
                d = int(e) - 1
                if row[i][d]:
                    return False
                if col[j][d]:
                    return False
                if square[i // 3][j // 3][d]:
                    return False
                row[i][d] = True
                col[j][d] = True
                square[i // 3][j // 3][d] = True
        return True
                
        