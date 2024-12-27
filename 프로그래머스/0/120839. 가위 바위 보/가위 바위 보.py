def solution(rsp):
    win_dict = {'2': '0', '0': '5', '5': '2'} 
    return ''.join(win_dict[i] for i in rsp)  