def legalmoves(board):
    moves = []
    for pos, piece in enumerate(board):
        jumpmove = pos + (piece * 2)
        move = pos + (piece)
        if (piece == 0):
            continue
        if (not ((jumpmove < 0) or (jumpmove >= len(board)))):
            if (board[jumpmove] == 0):
                t = list(board)
                t[pos] =0
                t[jumpmove]= piece
                moves.append(t)
        if (not((move <0) or (move >= len(board)))):
            if (board[move]==0):
                t= list(board)
                t[pos]=0
                t[move] = piece
                moves.append(t)
    return moves

def evalall(current, target):
    next = []
    for a in current:
        n = legalmoves(a[-1])
        for q in n:
            t = list(a)
            t.append(q)
            if(q==target):
                return t
            next.append(t)
    return next

def solve(start):
    temp= [[start]]
    end = list(start)
    end.reverse()
    while(temp[-1] != end):
        temp = evalall(temp, end)
    return temp

print(solve([1,1,1,0,-1,-1,-1]))


