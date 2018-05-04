def prStr():
    s = 'num1: {0} num2: {1}'.format(100,200)
    print(s)
    s = '{0:<10}-{1:<10}-{2:<10}'.format('apple','banana','grape')
    print(s)
    s = '{0:>10}-{1:>10}-{2:>10}'.format('apple','banana','grape')
    print(s)
    s = '{0:>1.10}'.format(3.14159265353579)
    print(s)
    #冒號後面規定印出的長度及左右對其規定
prStr()