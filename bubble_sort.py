numbers = [15, 3, 10, 3, 4, 1, 23, 2, 100, 23, 123, 41, 42, 89]

def bubble_sort(numbers):
    i = 1
    while i < len(numbers):
        if numbers[i] >= numbers[i-1]:
            i += 1
        else:
            numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
            i = 1
    
    return numbers

print(bubble_sort(numbers))