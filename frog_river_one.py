def solution(X, A):
    # write your code in Python 3.6
    river = set()
    for i in range(1, X+1):
        river.add(i)
    
    for idx in range(len(A)):
        if A[idx] in river:
            river.remove(A[idx])
        if len(river) == 0:
            return idx
    
    return -1
