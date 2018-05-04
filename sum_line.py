import sys
def sum_line():
    for line in sys.stdin:
        #line = line.strip()
       # print(line)
        tokens = line.split()
        print(tokens)
        #print(len(tokens))
        tot = 0
        for i in range(0,len(tokens)):
            float(tokens[i])
            tot = float(tokens[i]) + tot
        print(tot)


sum_line()