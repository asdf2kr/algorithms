# Fail.

'''
c = int(input())
for _ in range(c):
    n = int(input())
    m = int(input())
    a, b = [], []
    a.append(list(map(int, input().split())))
    b.append(list(map(int, input().split())))
    jlis(a, b)
'''
def lis(index):
    global data
    output = 1
    if index == len(data):
        return 0
    for i in range(index+1, len(data)):
        if data[index] < data[i]:
            output = max(output, lis(i) + 1)
    return output

def jlis(ind_a, ind_b):
    global a, b, mem

    if mem[ind_a][ind_b] != -1:
        return mem[ind_a][ind_b]
    output = 2

    if ind_a == 0 and ind_b == 0:
        _max = 0
    else:
        _max = max(a[ind_a], b[ind_b])

    for i in range(ind_a, len(a)):
            if _max < a[i]:
                output = max(output, jlis(i, ind_b) + 1)
    for j in range(ind_b, len(b)):
            if _max < b[j]:
                output = max(output, jlis(ind_a, j) + 1)
    mem[ind_a][ind_b] = output
    return output

c = int(input())
for _ in range(c):
    max_value = 0
    n = list(map(int, input().split())) # n[0] = n , n[1] = m
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mem = [ [ -1 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    output = 0
    for i in range(len(a)):
        output = max(output, jlis(i, 0))
    for j in range(len(b)):
        output = max(output, jlis(0, j))
    print(output)
