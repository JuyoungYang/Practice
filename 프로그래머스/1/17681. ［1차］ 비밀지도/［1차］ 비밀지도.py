def solution(n, arr1, arr2):
    result = []
    
    for i in range(n):
        # bin()으로 이진수 바꾸고 OR연산, 오비 빼야하니까 슬라이싱
        binary = bin(arr1[i] | arr2[i])[2:] 
        
        # 앞에 0 넣기
        binary = binary.zfill(n)
        
        # 1->#, 0->공백
        row = binary.replace('1', '#').replace('0', ' ')
        result.append(row)
    
    return result