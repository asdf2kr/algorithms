
# initial code

import math
def same(data, count, value):
    for i in range(len(data)):
        data[i] += value
    return data.count(data[0]) == count

def check(data, count):
    diff = data[1] - data[0]
    if same(data, count, 0): return 1
    elif (same(data, count, 1) | same(data, count, -1)): return 2
    elif (same(data[0::2], math.ceil(count/2), 0) | same(data[1::2], math.floor(count/2), 0)): return 4
    elif same(data, count, diff) : return 5
    else: return 10

def pi(index, count):
    global number, mem

    if mem[index] != -1:
        return mem[index]

    answer = check(number[index:index+count], count)
    i = index + count
    if i < len(number):
        ans_3 = pi(i, 3)
        ans_4 = pi(i, 4)
        ans_5 = pi(i, 5)
        answer = min(ans_3, ans_4, ans_5) + answer
        mem[index] = answer
    else:
        mem[index] = -1
        return float('inf')

    return answer

c = int(input())
for _ in range(c):
    num = input().strip()
    number = []
    for n in num:
        number.append(int(n))
    answer = float('inf')
    mem = [-1 for _ in range(len(number) + 1)]
    print(pi(0, 3), pi(0, 4), pi(0, 5))
    print(min(pi(0, 3), pi(0, 4), pi(0, 5)))
