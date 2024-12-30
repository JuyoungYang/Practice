def calculate_gpa(subjects):
    grade_points = {
        'A+': 4.5, 'A0': 4.0,
        'B+': 3.5, 'B0': 3.0,
        'C+': 2.5, 'C0': 2.0,
        'D+': 1.5, 'D0': 1.0,
        'F': 0.0
    }
    
    total_credit_points = 0  
    total_credits = 0       
    
    for subject in subjects:
        name, credit, grade = subject.split()
        credit = float(credit)
        
        if grade == 'P':
            continue
            
        total_credit_points += credit * grade_points[grade]
        total_credits += credit
    
    if total_credits == 0:
        return 0.0
    
    gpa = total_credit_points / total_credits
    return gpa

subjects = []
for _ in range(20):
    subjects.append(input())

result = calculate_gpa(subjects)
print(result)