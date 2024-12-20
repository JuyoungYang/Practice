def solution(arr):
    result = []
    for x in arr:
        if x >= 50 and x % 2 == 0:  
            result.append(x // 2)  
        elif x < 50 and x % 2 != 0:  
            result.append(x * 2)  
        else:
            result.append(x) 
    return result
