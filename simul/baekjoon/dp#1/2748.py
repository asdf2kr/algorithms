def fib(ind):
    global mem

    if ind == 0 or ind == 1:
        return 1
    if mem[ind] != -1:
        return mem[ind]
    val = mem[ind] = fib(ind-1) + fib(ind-2)
    return val

n = int(input())
mem = [-1 for _ in range(n+1)]
print(fib(n-1))
