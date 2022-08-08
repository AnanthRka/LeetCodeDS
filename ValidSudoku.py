def isValidSudoku(board: list[list[str]]) -> bool:

    #rows
    for r in range(9):
        rows = [c for c in board[r] if c!= '.']
        if len(rows)!= len(set(rows)): return False
    
    #columns
    for c in range(9):
        cols = [board[r][c] for r in range(9) if board[r][c]!='.']
        if len(cols)!= len(set(cols)): return False

    #3x3boxes
    def helper(R,C):
        
        l = set()

        for r in range(R,R+3):
            for c in range(C,C+3):
                if board[r][c]== '.': continue
                if board[r][c] not in l:
                    l.add(board[r][c])
                else:
                    return False
        return True

    for i in range(0,9,3):
        for j in range(0,9,3):
            if not helper(i,j):
                return False
    return True


print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))