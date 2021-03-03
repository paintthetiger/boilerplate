# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    if N < 4:
        return 0

    top_score = 0
    current_score = 0
    counting = False
    ready = False

    remain = N
    while remain != 0:
        r = remain % 2 # 1 0 0 0 1
        if ready:
            if r == 1:
                counting = False
            else:
                ready = False

        if r == 1:
            if counting:
                if current_score > top_score:
                    top_score = current_score

                ready = True
                current_score = 0
            else:
                counting = True
        else:
            if counting:
                current_score += 1
        
        remain = math.floor(remain / 2) # 520 260 130 65 32
    
    if current_score > top_score:
        top_score = current_score
    # write your code in Python 3.6
    return top_score
