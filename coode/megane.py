N = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
middle_index = (N + 1) // 2
middle_number = numbers[middle_index - 1]
print(middle_number)

