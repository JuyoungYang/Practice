def solution(s):
    numbers = list(map(int, s.split()))
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    answer = f"{min_val} {max_val}"
    
    return answer