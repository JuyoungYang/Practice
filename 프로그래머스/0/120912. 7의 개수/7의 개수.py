def solution(array):
    answer = 0
    for num in array:
        for digit in str(num):
            if digit == '7':
                answer += 1
    return answer