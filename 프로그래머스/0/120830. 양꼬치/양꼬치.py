def solution(n, k):
    #양꼬치 n*12000, (k-(n//10))*2000
    answer = (n * 12000) + ((k - (n // 10)) * 2000)
    return answer