def func2(diclist):
    val = []
    key = input('Tell me the dictionary key you want check')
    for dict in diclist:
        val.append(dict[key])
    return val



dict1 = {'a':1,'b':3, 'c':4}

dict2 = {'d':3,'a':1,'c':3}

dict3 = {'a':90,'x':90,'b':2}



try:
    print(func2([dict1, dict2, dict3]))
except KeyError:
    print('You must enter a key that exists in all the dictionaries')






















