def solution(A, K):
    # write your code in Python 3.6
    if len(A) < 2:
        return A

    real_rotate = K % len(A)

    result = list()

    for index in range(len(A) - real_rotate, len(A) - real_rotate + len(A)):
        real_index = (index + real_rotate) % len(A)
        result.append(A[index % len(A)])


    return result
