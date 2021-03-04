def solution(X, Y, D):
    dis = Y - X
    if X == Y:
        return 0
    elif dis <= D:
        return 1
    else:
        jump = dis // D
        return jump + 1 if dis % D else jump

