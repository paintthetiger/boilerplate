def solution(A):
    sample = dict()

    for ele in A:
        if sample.get(ele):
            sample.pop(ele)
        else:
            sample[ele] = 1
    
    for k in sample.keys():
        return k
        

    # write your code in Python 3.6
    # pass


# 9 3 7 9 2 2 4 5 5 4 -> 7
