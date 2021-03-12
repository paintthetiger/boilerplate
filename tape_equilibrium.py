def solution(A):
    # write your code in Python 3.6
    total_sum = 0

    for el in A:
        total_sum += el

    min_result = None
    for el in range(len(A) -1):
        difference = total_sum - (A[el] * 2)
        result = abs(difference)
        if min_result is None or result < min_result:
            min_result = result

        total_sum = difference

    return min_result
