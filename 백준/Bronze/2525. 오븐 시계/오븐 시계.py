h, m = map(int, input().split()) 
r = int(input())  

h += (m + r) // 60  
m = (m + r) % 60  

if h >= 24:
    h -= 24

print(h, m)
