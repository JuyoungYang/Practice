def solution(s):
    stack = []
    # 공백으로 분리
    numbers = s.split()
    
    # 각 요소를 순회
    for num in numbers:
        if num == 'Z':
            # Z를 만나면 직전 숫자를 스택에서 제거
            if stack:  # 스택이 비어있지 않은 경우에만
                stack.pop()
        else:
            # 숫자는 정수로 변환하여 스택에 추가
            stack.append(int(num))
    
    # 스택에 남은 모든 숫자의 합을 반환
    return sum(stack)