from collections import Counter

def solution(array):
    count = Counter(array)  # array에서 각 값의 빈도 계산
    most_common = count.most_common(2)  # 가장 자주 나오는 값 2개를 가져옴
    
    # 만약 가장 자주 나오는 값이 2개 이상이고 그 값들이 같다면 -1을 반환
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    return most_common[0][0]  # 최빈값 반환