'''
# JumpGame in Algospot. (using Dynamic programming)
# If you solve this problem in Algospot, you use the graph method.
board = []
mem = []
def jump(i, j):
    global board
    if i == 0 and j == size-1: return True
    elif i < 0 or j >= size or mem[i][j] == False: return False

    value = board[i][j]
    ret = jump(i - value, j) | jump(i, j + value)
    mem[i][j] = ret
    return ret

t = int(input())
for i in range(t):
    size = int(input())

    for _ in range(size):
        board.insert(0, (list(map(int, input().split()))))
        mem.insert(0, [True for _ in range(size)])
    # Solve.
    if jump(size-1, 0):
        print("YES")
    else:
        print("NO")
'''

