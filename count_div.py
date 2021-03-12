# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):

    start = A // K
    end = B // K

    answer = end - start

    if not A % K:
        answer += 1

    return answer
