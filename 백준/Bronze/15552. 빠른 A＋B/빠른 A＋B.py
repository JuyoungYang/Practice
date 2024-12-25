import sys

# 입력의 첫 번째 줄에서 테스트케이스 개수를 읽음
T = int(sys.stdin.readline().rstrip())  

# 각 테스트케이스 처리
for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())  # 두 정수 A, B 입력
    sys.stdout.write(f"{A + B}\n")  # 결과 출력
