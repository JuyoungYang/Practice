str, n = input().strip().split(' ')
n = int(n)
def repeat_string(str, n):
    if 1 <= len(str) <= 10 and 1 <= n <= 5:
        return str * n  
    else :
        return "조건에 맞지 않는 입력입니다."
print(repeat_string(str, n))