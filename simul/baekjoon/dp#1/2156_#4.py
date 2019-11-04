'''
# initial code.
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
mem = [-1 for _ in range(10001)]

if n <= 3:
    print(sum(data))
else:
    mem[0] = data[0]
    mem[1] = data[0] + data[1]
    mem[2] = max(mem[0], mem[1]) + data[2]
    for i in range(3, n):
        mem[i] = max(mem[i-1] + mem[i-3], mem[i-2] + mem[i-3]) + data[i]
    print(mem[:n])
'''


n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))
mem = [0 for _ in range(10002)]

if n == 1:
    print(data[1])
elif n == 2:
    print(data[1] + data[2])
elif n == 3:
    print(max(max(data[2], data[3]) + data[1], data[2] + data[3]))
else:
    mem[1] = data[1]
    mem[2] = data[1] + data[2]
    mem[3] =max(max(data[2], data[3]) + data[1], data[2] + data[3])
    for i in range(4, n + 1):
        mem[i] = max(data[i] + data[i-1] + mem[i-3], data[i] + mem[i-2], mem[i-1])
    print(mem[n])
