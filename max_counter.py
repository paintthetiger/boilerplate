# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # First try
    # counters = [0] * N
    # max_value = 0
    # for el in A:
    #     if el > N:
    #         counters = [max_value] * N
    #     else:
    #         counters[el - 1] += 1
    #         if counters[el - 1] > max_value:
    #             max_value = counters[el - 1]  

    # return counters

    # Second try
    command = dict()
    totla_max_value = 0
    current_max_value = 0
    for el in A:
        if el > N:
            totla_max_value += current_max_value
            current_max_value = 0
            command = dict()
        else:
            if (el - 1) in command:
                command[el-1] += 1
            else:
                command[el-1] = 1
            if command[el-1] > current_max_value:
                current_max_value = command[el-1]

    answer = [totla_max_value] * N
    for key, amount in command.items():
        answer[key] += amount 

    return answer
