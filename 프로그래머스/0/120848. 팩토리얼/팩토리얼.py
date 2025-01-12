def solution(n):
    factorial = 1
    i = 1
    
    while True:
        factorial *= i
        
        if factorial > n:
            return i - 1
            
        i += 1