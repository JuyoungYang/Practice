def solution(num_list):
    odd_str = ""  #홀수
    even_str = "" #짝수

    for num in num_list:
        if num % 2 == 0:  # 짝수
            even_str += str(num)
        else:  # 홀수
            odd_str += str(num)
    
    return int(odd_str) + int(even_str)