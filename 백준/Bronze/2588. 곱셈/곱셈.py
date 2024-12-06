# 입력 받기
num1 = int(input())
num2 = int(input())

# 두 번째 숫자의 각 자리 숫자
digit1 = num2 % 10          # 1의 자리
digit2 = (num2 // 10) % 10  # 10의 자리
digit3 = num2 // 100        # 100의 자리

# 곱셈 과정
result1 = num1 * digit1
result2 = num1 * digit2
result3 = num1 * digit3
final_result = num1 * num2

# 출력
print(result1)
print(result2)
print(result3)
print(final_result)