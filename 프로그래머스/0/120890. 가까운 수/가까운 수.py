def solution(array, n):
    # 초기값: 가장 가까운 수를 배열의 첫 번째 요소로 설정
    closest = array[0]
    
    for num in array:
        # 현재 수와 n의 차이
        diff_current = abs(num - n)
        # 가장 가까운 수와 n의 차이
        diff_closest = abs(closest - n)

        # 차이가 더 작거나, 차이가 같을 때 더 작은 수인 경우 갱신
        if diff_current < diff_closest or (diff_current == diff_closest and num < closest):
            closest = num

    return closest