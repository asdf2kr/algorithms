
'''
# WildCard in Alogospot.
# First method.
def match(wc, name):
    pos = 0
    while(pos < len(wc) and pos < len(name)) and (wc[pos] == '?' or wc[pos] == name[pos]):
        pos += 1
    if pos == len(wc):
        return pos == len(name)

    if wc[pos] == '*':
        for skip in range(0, len(name)):
            if match(wc[pos+1:], name[pos+skip:]):
                return True
    return False

test_case = int(input())
for _ in range(test_case):
    wc = str(input())
    n = int(input())

    fileName = []
    answer = []
    check = [True for _ in range(n)]
    for _ in range(n):
        fileName.append(str(input()))

    for i in range(n):
        if match(wc, fileName[i]):
            answer.append(fileName[i])

    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
'''
'''
# Second method.
def match(w_pos, f_pos):
    global file_, wc, mem
    ret = int(mem[w_pos][f_pos])
    if ret != -1:
        return mem[w_pos][f_pos]

    while(w_pos < len(wc) and f_pos < len(file_)) and (wc[w_pos] == '?' or wc[w_pos] == file_[f_pos]):
        w_pos += 1
        f_pos += 1

    if w_pos == len(wc):
        return_ = mem[w_pos][f_pos] = (f_pos == len(file_))
        return return_

    if wc[w_pos] == '*':
        for skip in range(0, len(file_)):
            if f_pos + skip > len(file_) or w_pos + 1 > len(wc):
                continue
            if match(w_pos+1, f_pos+skip):
                return_ = mem[w_pos][f_pos] = True
                return return_
    return_ = mem[w_pos][f_pos] = False
    return return_

test_case = int(input())
for _ in range(test_case):
    wc = str(input())
    n = int(input())

    file_ = None
    fileName = []
    answer = []

    check = [True for _ in range(n)]
    for _ in range(n):
        fileName.append(str(input()))

    for i in range(n):
        file_ = fileName[i]
        mem = [ [-1 for _ in range(len(file_)+ 1)] for _ in range(len(wc)+ 1)]
        if match(0, 0):
            answer.append(file_)

    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
'''
# Third method.

