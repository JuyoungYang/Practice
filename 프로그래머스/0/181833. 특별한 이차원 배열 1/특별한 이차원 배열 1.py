def solution(n):
    arr = []
    
    for i in range(n):
        row = []  
        for j in range(n):
            if i == j:  
                row.append(1)
            else:  
                row.append(0)
        arr.append(row)  
    
    return arr