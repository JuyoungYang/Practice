def solution(my_string, index_list):
    newstr = []
    for index in index_list:
        newstr.append(my_string[index])
        
    return ''.join(newstr)