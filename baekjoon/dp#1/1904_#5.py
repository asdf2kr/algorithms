
n = int(input())
mem = [-1 for _ in range(n+1)]
mem[0], mem[1], mem[2] = 1, 1, 2
for i in range(3, n+1):
    mem[i] = mem[i-2] + mem[i-1]
    mem[i] %= 15746
print(mem[i])
