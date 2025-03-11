def solution(num, k):
    num_str = str(num)  
    k_str = str(k)  
    index = num_str.find(k_str)  
    
    return index + 1 if index != -1 else -1