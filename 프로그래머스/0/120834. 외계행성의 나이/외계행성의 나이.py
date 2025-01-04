def solution(age):
    num_to_alpha = {
        '0': 'a', '1': 'b', '2': 'c', '3': 'd', 
        '4': 'e', '5': 'f', '6': 'g', '7': 'h', 
        '8': 'i', '9': 'j'
    }
    
    age_str = str(age)
    
    return ''.join(num_to_alpha[digit] for digit in age_str)