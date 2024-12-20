#1. 사용자의 이름을 입력받아 "안녕하세요, [이름]님!"이라고 출력하는 함수 **`say_hello`**를 작성하세요.
# name = input("이름 입력: ")
# def say_hello():
#     print(f"안녕하세요, {name}님!")
# say_hello()


#2. 두 개의 숫자를 입력받아 큰 수를 반환하는 함수 **`find_larger`**를 작성하세요.
# num1, num2 = map(int, input().split())
# def find_larger(num1, num2):
#     return num1 if num1 > num2 else num2
# print(find_larger(num1, num2))




#3. 리스트를 입력받아 그 리스트의 첫 번째 요소와 마지막 요소를 출력하는 함수 **`print_first_last`**를 작성하세요.
# lst = [10, 20, 30, 40, 50]
# def print_first_last(lst):
#     if len(lst) == 0:
#         print("깡통")
#     else:
#         print(f"첫 번째 요소: {lst[0]}")
#         print(f"마지막 요소: {lst[-1]}")
# print_first_last(lst)


#4. 숫자를 하나 입력받아 그 숫자가 짝수인지 홀수인지 출력하는 함수 **`even_or_odd`**를 작성하세요.
# number = int(input())
# def even_or_odd(number):
#     if number % 2 == 0:
#         print(f"{number}는 짝수")
#     else:
#         print(f"{number}는 홀수")
# even_or_odd(number)


#5. 문자열을 입력받아 그 문자열을 대문자로 변환하여 반환하는 함수 **`to_uppercase`**를 작성하세요.
# string = str(input())
# def to_uppercase(string):
#     return string.upper()
# print(to_uppercase(string))


#6. 두 숫자를 입력받아 더한 결과를 반환하는 함수 **`add_numbers`**를 작성하세요.
# num1, num2 = map(int, input().split())
# def add_numbers(num1, num2):
#     return num1 + num2
# print(add_numbers(num1, num2))


#7. 리스트를 입력받아 모든 요소의 합을 반환하는 함수 **`sum_list`**를 작성하세요. (내장 함수 sum을 사용하지 않고 구현해보세요.)
# lst = [10, 20, 30, 40, 50]
# def sum_list(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total
# print(sum_list(lst))


#8. 임의의 개수의 숫자를 입력받아 그 평균을 계산하는 함수 **`calculate_average`**를 작성하세요. (가변 인자를 사용하세요.)
# def calculate_average():
#     user_input = input()
#     numbers = [int(num) for num in user_input.split()]
#     if len(numbers) == 0:
#         return "숫자를 입력해주세요."
#     total = sum(numbers)  
#     return total / len(numbers)  
# result = calculate_average()
# print(result)



#9. 문자열을 입력받아 그 문자열의 길이를 반환하는 람다 함수를 작성하세요.
# string = str(input())
# length_of_string = lambda x: len(x) 
# print(length_of_string(string))



#10. 딕셔너리를 입력받아 키와 값을 바꾼 새로운 딕셔너리를 반환하는 함수 **`swap_dict`**를 작성하세요.
# def swap_dict(input_dict):
#     return {v: k for k, v in input_dict.items()}



#11. 기본 매개변수를 사용하여 인사말을 출력하는 함수 **`greet`**를 작성하세요. 이름이 주어지지 않으면 "Guest"라고 인사하도록 합니다.
# #name = input("이름 입력하세유(싫으면 안해도 댐): ")
# def greet(name=None):
#     if name is None:
#         name = "Guest"
#     print(f"안녕하세요, {name}님!")
# #greet()



#빠진문제. 재귀 함수를 사용하여 팩토리얼(n!)을 계산하는 함수 **`factorial`**을 작성하세요.