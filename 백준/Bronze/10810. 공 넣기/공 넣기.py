N, M = map(int, input().split())
baskets = [0] * (N+1)  

for _ in range(M):
    i, j, k = map(int, input().split())
    for basket in range(i, j+1):
        baskets[basket] = k

print(' '.join(map(str, baskets[1:])))