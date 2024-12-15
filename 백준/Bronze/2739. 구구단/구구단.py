N = int(input())
1<=N<=9
result = []  
for i in range(1, 10): 
    result.append(N * i)
    print(f"{N} * {i} = {N * i}") 