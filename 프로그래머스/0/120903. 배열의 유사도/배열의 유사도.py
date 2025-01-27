def solution(s1, s2):
    count = 0
    for element in s1:
        if element in s2: 
            count += 1
    return count
