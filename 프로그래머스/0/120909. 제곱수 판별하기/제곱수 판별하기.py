def solution(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return 1
        i += 1
    return 2