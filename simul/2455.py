def main():
    maxNum = 0
    num = 0
    for i in range(0, 4):
        a = input()
        b = input()
        num -= a
        num += b
        if maxNum < num:
            maxNum = num
if __name__== '__main__':
    main()
