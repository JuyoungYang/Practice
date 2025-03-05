def solution(myString, pat):
    trans_table = str.maketrans("AB", "BA")
    converted = myString.translate(trans_table)
    
    return 1 if pat in converted else 0
