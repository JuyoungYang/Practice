def solution(num_list):
    last_element = num_list[-1]
    second_last_element = num_list[-2]
    if last_element>second_last_element:
        num_list.append(last_element-second_last_element)
    else : 
        num_list.append(last_element*2)
    return num_list