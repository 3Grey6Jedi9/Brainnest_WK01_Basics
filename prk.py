
strlist = ["r","1.2",'d','2.3','a']
j = 0
new = []
for i in strlist:
    try:
        new.append(float(i))
    except ValueError:
        print(f'Impossible to convert the value "{i}" with the index {j} into a float')
        j +=1
        continue
    else:
        j +=1

print(new)

for n in strlist:
    print(type(n), strlist)












