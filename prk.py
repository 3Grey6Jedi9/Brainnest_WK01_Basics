intlist = []
total = []
program = True
while program:
    choice = int(input('Enter a element of the list please'))
    intlist.append(choice)
    cont = input('Enter "N" if you are done with your list. Otherwise press any other key to continue').lower()
    if cont == 'n':
        program = False
for i in intlist:
    if (i % 2) == 0:
        total.append(i)
    else:
        continue

print(sum(total), intlist)






