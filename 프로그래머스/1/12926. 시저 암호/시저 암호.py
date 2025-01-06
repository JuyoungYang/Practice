def solution(s, n):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    answer = ''
    for char in s:
        if char == ' ':   
            answer += ' '
        elif char.isupper():    
            idx = upper.index(char)    
            answer += upper[(idx + n) % 26]  
        else:    
            idx = lower.index(char)
            answer += lower[(idx + n) % 26]

    return answer