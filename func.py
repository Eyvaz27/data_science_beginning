def func1(element):
    # r = []
    print('Func1 is called')
    for i in element:
        if(i !=0 and i % 2 == 0):
            # r.append(i)
            print(i)
    # return r


def func2(element):
    # r = []
    print('Func2 is called')
    for i in element:
        if(i != 0 and bin(i)[2:][len(bin(i)[2:]) - 1] == '0'):
            # r.append(i)
            print(i)
    # return r
