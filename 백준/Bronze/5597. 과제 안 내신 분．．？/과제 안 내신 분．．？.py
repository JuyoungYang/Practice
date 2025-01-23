def find_missing_students():
    # 제출자 출석번호
    submitted = {int(input()) for _ in range(28)}
    
    # 1~30 중 제출되지 않은 번호찾기
    all_students = set(range(1, 31))
    missing = sorted(all_students - submitted)
    
    print(missing[0])
    print(missing[1])

find_missing_students()