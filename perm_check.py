# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    perm_check = set()
    
    for el in A:
        perm_check.add(el)

        if el > len(A):
            return 0

    return 1 if len(perm_check) == len(A) else 0
