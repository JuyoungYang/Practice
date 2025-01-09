numbers = []
for _ in range(9):
    numbers.append(int(input()))

max_value = numbers[0]
max_index = 1

for i in range(9):
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i + 1

print(max_value)
print(max_index)