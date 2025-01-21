def solution(my_string):
    answer = [int(char) for char in my_string if char.isdigit()]
    answer.sort()
    return answer