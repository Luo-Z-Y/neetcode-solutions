class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # three sets to record if the number appeared twice
        row_record = list(set() for _ in range(9))
        col_record = list(set() for _ in range(9))
        patch_record = list(set() for _ in range(9))

        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == ".":
                    continue
                elif cur not in row_record[row] and cur not in col_record[col] and cur not in patch_record[3*(row//3) + col//3]:
                    row_record[row].add(cur)
                    col_record[col].add(cur)
                    patch_record[3*(row//3) + col//3].add(cur)
                else:
                    return False
        return True