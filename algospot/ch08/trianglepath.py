
def max_path(height, width):
    global n

    if height == n-1: return tri[height][width]

    if mem[height][width] != -1:
        return mem[height][width]

    max_value = mem[height][width] = tri[height][width] + max(max_path(height+1, width+1), max_path(height+1, width))

    return max_value

c = int(input())
for _ in range(c):
    n = int(input())
    tri = []
    mem = [[ -1 for _ in range(n) ] for _ in range(n)]
    for _ in range(n):
        tri.append(list(map(int, input().split())))
    print(max_path(0, 0))
