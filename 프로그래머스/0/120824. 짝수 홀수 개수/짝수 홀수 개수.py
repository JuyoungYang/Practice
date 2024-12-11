def solution(num_list):
    two = sum(1 for num in num_list if num % 2 == 0) 
    one = sum(1 for num in num_list if num % 2 != 0)  
    return (two, one)