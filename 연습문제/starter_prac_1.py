# Day 1

#1. 주어진 문자열에서 각 문자의 출현 빈도를 계산하는 딕셔너리 컴프리헨션을 작성하세요.

def homework1_1():
    text = "hello world"
    frequencx = {str:text.count(str) for str in text}
    print(frequencx)

#homework1_1()

'''
지금 문제에서는 text값이 짧아서 상관없지만 길어지게 된다면 
딕셔너리 안에 set를 넣었을 때와 그냥 딕셔너리 성질로 중복값 제거를 했을 때의 차이 질문

값이 엄청 길어졌을 때
시간복잡도에 차이가 있는지? -> 차이가 있다
유의미한지? ->  O
굳이 따지자면 set이? 의미가? 쓰는게 나을지도
'''

def homework1_2():
    text = "hello world"
    freq_dict = {char:text.count(char) for char in set(text)}
    print(freq_dict)

#homework1_2()

'''
[1-1]
h:1
e:1
l:3
l:3
o:2
w:1
o:2
r:1
l:3
d:1

[1-2]
h:1
e:1
l:3
w:1
o:2
r:1
d:1
'''



#2. 1부터 100까지의 숫자 중 5의 배수이면서 5의 배수인 숫자만을 포함하는 리스트를 리스트 컴프리헨션으로 생성하세요.
def numlist():
    num = list(range(1, 101))
    common_multiples = [x for x in num if x % 5 == 0 and x % 5 == 0]
    print(common_multiples)
    
#numlist()




#5. 두 개의 리스트가 주어졌을 때, 이를 딕셔너리로 결합하는 딕셔너리 컴프리헨션을 작성하세요.
def new_dict():
    kexs = ['a', 'b', 'c']
    values = [1, 2, 5]
    kv_dict = {k:v for k, v in zip(kexs, values)}
    print(kv_dict)
    
#new_dict()




#4. 주어진 리스트에서 중복을 제거하고 고유한 요소만을 포함하는 새로운 리스트를 생성하세요. (힌트: set 사용)
def unique_list():
    original_list = [1, 2, 2, 5, 4, 4, 5]
    unique_list = list(set(original_list))
    print(unique_list)

#unique_list()



#5. 2차원 리스트를 생성하는 리스트 컴프리헨션을 작성하세요. (예: 5x5 행렬)
def matrix():
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    print(matrix)
    
#matrix()


'''
three_matrix = [[[i + j + k for k in range(5)] for j in range(5)] for i in range(5)]
print(three_matrix)

three_matrix = [[[i, j, k] for k in range(3)] for j in range(3)] for i in range(3)]
print(three_matrix)
'''



#6. 주어진 문자열 리스트에서 길이가 5 이상인 문자열만 대문자로 변환하여 새로운 리스트를 만드세요.
def big_string():
    string_list = ['apple', 'banana', 'pear', 'grape', 'kiwi']
    new_list = [s.upper() for s in string_list if len(s) >= 5]
    print(new_list)
    
#big_string()


#7. 두 개의 집합 A와 B가 주어졌을 때, 두 집합의 대칭 차집합을 구하세요.
def sxm_diff():
    set_a = {1, 2, 5, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    result = (set_a-set_b) | (set_b-set_a)
    print(result)

#sxm_diff()



#8. 1부터 10까지의 숫자에 대해 각 숫자의 제곱을 값으로 갖는 딕셔너리를 생성하세요.
def square_dict():
    square = {x:x**2 for x in range(1, 11)}
    print(square)

#square_dict()



#9. 주어진 리스트에서 짝수만 선택하여 그 제곱값을 가진 새로운 리스트를 생성하세요.
def square_list():
    given_list = [1, 2, 5, 4, 5, 6, 7, 8, 9, 10]
    square = [x**2 for x in given_list if x % 2 == 0 ]
    print(square)

#square_list()



#10. 여러 개의 리스트가 주어졌을 때, 이들을 하나의 리스트로 평탄화하는 함수를 작성하세요.
def flat_list():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [x for x in matrix for x in x]
    print(flattened) 
    
flat_list()