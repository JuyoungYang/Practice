def solution(s):
    mid = len(s) // 2

    #짝
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]  
    #홀
    else:  
        return s[mid] 
