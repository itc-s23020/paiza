M, N = map(int, input().split())
steps_forward = M - N
if steps_forward <= 0:
    print(0)
else:
    print(steps_forward)

