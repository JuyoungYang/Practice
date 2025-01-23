def swap_balls(N, swaps):
    baskets = list(range(1, N + 1))
    for i, j in swaps:
        baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]
    return baskets

N, M = map(int, input().split())
swaps = [tuple(map(int, input().split())) for _ in range(M)]
result = swap_balls(N, swaps)
print(*result)