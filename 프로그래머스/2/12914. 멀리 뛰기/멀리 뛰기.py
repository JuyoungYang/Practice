def solution(n):
    MOD = 1234567  # 나머지를 구할 값
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)  # DP 테이블 초기화
    dp[1], dp[2] = 1, 2  # 초기 값 설정

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD  # 점화식 적용 및 나머지 계산

    return dp[n]
