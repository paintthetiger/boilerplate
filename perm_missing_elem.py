def solution(A):
    N = len(A) + 1
    remain = N % 2
    if not remain:
        target =(N + 1) * (N // 2)
    else:
        target = (N * (N // 2)) + N

    sum_s = 0
    for el in A:
        sum_s += el

    return target - sum_s

:
