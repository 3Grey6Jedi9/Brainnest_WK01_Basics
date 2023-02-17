
def func3(intlist):
    try:
        for n in intlist:
            if type(n) is not int:
                raise TypeError('Only integers please')
    except TypeError as err:
        print(f'{err}')
    else:
        return max(intlist)


a = func3([1,2,3,2.3])

print(a)






















