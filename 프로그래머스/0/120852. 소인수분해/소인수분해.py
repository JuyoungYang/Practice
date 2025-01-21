def solution(n):
    factors = set()  # 소인수를 저장할 집합
    divisor = 2  # 2부터 시작하여 나눔
    while n > 1:
        if n % divisor == 0:  # 나누어떨어지는 경우
            factors.add(divisor)  # 소인수로 추가
            n //= divisor  # n을 해당 소인수로 나눔
        else:
            divisor += 1  # 다음 수로 진행
    return sorted(factors)  # 오름차순 정렬하여 반환
