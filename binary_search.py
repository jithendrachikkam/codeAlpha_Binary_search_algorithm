def generate_range(start, end, step):
    numbers = []
    current = start
    while current <= end:
        numbers.append(current)
        current += step
    return numbers

start = 0
end = 20
step = 2
result = generate_range(start, end, step)
print(result)
