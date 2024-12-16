import re

def solution(babbling):
    possible_sounds = ["aya", "ye", "woo", "ma"]
    
    count = 0
    
    for word in babbling:
        # 단어에 사용된 발음이 정확히 "aya", "ye", "woo", "ma"만 있어야 한다.
        word = re.sub(r'aya|ye|woo|ma', '', word)  # 발음만 제거
        if word == '':  # 발음만 남았다면
            count += 1
    
    return count