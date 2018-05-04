def ticket1(age):
    if age < 15:
        print('kid')
    elif age < 65:
        print('adult')
    else:
        print('senior')
def t2(age):
    if age < 15: print('kid')
    elif age < 65: print('adult')
    else: print('senior')
def t3(age):
    tickettype = 'kid' if age < 15 else 'adult' if age < 65 else 'senior'
    print(tickettype)
def test():
    ticket1(10)
    ticket1(20)
    ticket1(70)
    t2(10)
    t2(20)
    t3(70)
    t3(10)
    t3(20)
    t3(70)
test()