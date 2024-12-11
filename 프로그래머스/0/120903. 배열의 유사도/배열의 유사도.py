def solution(s1, s2):
    num = sum(1 for char in s1 if char in s2)
    return num