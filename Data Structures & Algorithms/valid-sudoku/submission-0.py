class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row and Col Test

        for i in range(9):
            row_seen = [0]*10
            col_seen = [0]*10

            for j in range(9):

                row_val = board[i][j]
                col_val = board[j][i]

                if row_val != ".":
                    if row_seen[int(row_val)] != 1:
                        row_seen[int(row_val)] = 1
                    else:
                        return False

                if col_val != ".":
                    if col_seen[int(col_val)] != 1:
                        col_seen[int(col_val)] = 1
                    else:
                        return False

        # 3*3 Box Test

        for k in range(9):
            print(k//3, 'i', 3*(k//3), 3*(k//3) + 3)
            print(k%3, 'j', 3*(k%3), 3*(k%3) + 3)

            val_seen = [0] * 10

            for i in range(3*(k//3), 3*(k//3) + 3):
                for j in range(3*(k%3), 3*(k%3) + 3):

                    val = board[i][j]

                    if val != ".":
                        if val_seen[int(val)] != 1:
                            val_seen[int(val)] = 1
                        else:
                            return False

        return True
        