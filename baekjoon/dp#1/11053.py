
def LIS(index):
    global data, mem
    num = 1
    if index == len(data):
        return 0

    if mem[index] != -1:
        return mem[index]

    for i in range(index + 1, len(data)):
        if data[index] < data[i]:
            num = max(num, LIS(i) + 1)
    mem[index] = num
    return num

n = int(input())
data = list(map(int, input().split()))
mem = [ -1 for _ in range(len(data))]
max_num = 0
for i in range(len(data)):
    max_num = max(LIS(i), max_num)
print(max_num)
