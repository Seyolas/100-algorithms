

def çözüm(x):
    string=str(x)
    if string[0]=='-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])


print(çözüm(-3232))