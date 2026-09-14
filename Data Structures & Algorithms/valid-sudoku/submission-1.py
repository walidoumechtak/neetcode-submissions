class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        i = 0
        while i < 9:
            j = 0
            seen = set()
            while j < 9:
                if board[j][i] == ".":
                    j += 1
                    continue
                if board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])
                j += 1
            i += 1
        
        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sq // 3) * 3 + i
                    col = (sq % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True


