t = int(input())
for _ in range(t):
    n = int(input())
    mem = [-1 for _ in range(101)]
    mem[0], mem[1], mem[2], mem[3], mem[4] = 1, 1, 1, 2, 2
    for i in range(5, n+1):
        mem[i] = mem[i-1] + mem[i-5]
    print(mem[n - 1])
