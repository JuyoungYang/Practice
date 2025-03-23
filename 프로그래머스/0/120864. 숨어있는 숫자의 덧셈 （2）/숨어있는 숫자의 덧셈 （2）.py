def solution(my_string):
    num_str = ''
    total_sum = 0
    
    for char in my_string:
        if char.isdigit():
            num_str += char
        else:
            if num_str:
                total_sum += int(num_str)
                num_str = ''
    
    if num_str:
        total_sum += int(num_str)
    
    return total_sum