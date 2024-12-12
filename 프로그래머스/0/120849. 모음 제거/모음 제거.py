def solution(my_string):
    exclude = ['a', 'e', 'i', 'o', 'u']
    answer = [x for x in my_string if x not in exclude]
    return ''.join(answer)