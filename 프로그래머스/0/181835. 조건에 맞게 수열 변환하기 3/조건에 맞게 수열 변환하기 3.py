def solution(arr, k):
    if k % 2 != 0:
        arr = [x * k for x in arr]
    else:
        arr = [x + k for x in arr]
    return arr