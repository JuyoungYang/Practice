def solution(my_string):
    unique_text = ''.join(dict.fromkeys(my_string))
    return unique_text