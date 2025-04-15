def solution(n):
    answer = 0
    count = 0 # 

    while count < n:
        answer += 1 

        is_multiple_of_3 = (answer % 3 == 0)

        contains_digit_3 = ('3' in str(answer))

        if not is_multiple_of_3 and not contains_digit_3:
            count += 1 
            
    return answer