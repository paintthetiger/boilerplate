# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    check = set()
    max_value = 0
    
    for el in A:
        if el > max_value:
            max_value = el
        check.add(el)

    candidate = 1
    while candidate != max_value:
        if candidate not in check:
            return candidate
        candidate += 1

    return max_value + 1
