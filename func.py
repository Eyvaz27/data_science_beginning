def func1(element):
    r = []
    for i in element:
        if(i % 2 == 0):
            r.append(i)
    return r


def func2(element):
    r = []
    for i in element:
        if(bin(i)[2:] == '0'):
            r.append(i)
    return r
