import sys

def readinput():
    line = input()
    cnt = int(line)
    for i in range(0, cnt):
        line = input()
        num = int(line)
        print(num+1)
readinput()

def readinput2():
    for line in sys.stdin:
        line = line.strip()
        num = int(line)
        print(num + 2) 
readinput2()