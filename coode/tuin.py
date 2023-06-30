s = int(input())
t = int(input())

progress = '-' * s
progress = progress[:t-1] + '+' + progress[t:]

print(progress)

