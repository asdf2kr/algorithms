def solve(ind, weight, value):
    global w, v, k, mem
    max_value = value

    if mem[ind][weight] != -1:
        return mem[ind][weight]

    if weight > k:
        return 0

    for i in range(ind+1, len(w)):
        weight += w[i]
        if weight <= k:
            max_value = max(max_value, solve(i, weight, value + v[i]))
        weight -= w[i]
    mem[ind][weight] = max_value
    return max_value

input_ = list(map(int, input().split()))
n, k = input_[0], input_[1]
w = []
v = []
for _ in range(n):
    input_ = list(map(int, input().split()))
    w.append(input_[0])
    v.append(input_[1])
max_value = 0
mem = [[-1 for _ in range(100001)] for _ in range(n)]
for i in range(n):
    max_value = max(max_value, solve(i, w[i],v[i]))
print(max_value)
'''
# Time & Error & memory param. ^ initial weight
def solve(ind, weight, value):
    global w, v, k
    max_value = value
    for i in range(ind, len(w)):
        now_weight = weight + w[i]
        if now_weight <= k:
            now_value = value + v[i]
            max_value = max(max_value, solve(i, now_weight, now_value))
    return max_value

input_ = list(map(int, input().split())) # int(input()), int(input())
n, k = input_[0], input_[1]
w = []
v = []
for _ in range(n):
    input_ = list(map(int, input().split()))
    w.append(input_[0])
    v.append(input_[1])
max_value = 0
for i in range(n):
    max_value = max(max_value, solve(i, w[i],v[i]))
print(max_value)
'''
