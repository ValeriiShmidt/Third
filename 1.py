from random import randint

lst1 = []
for x in range(25):
    lst1.append(randint(0, 9))

lst2 = []
for x in range(35):
    lst2.append(randint(0, 9))

for x in lst1:
    print(x, end=' ')
print()

for x in range(len(lst1)):
    if x % 20 < 9:
        print(lst1[x], end=' ')
    elif x % 20 == 9:
        print(lst1[x])
    elif x % 20 == 19:
        print(lst1[29 - x])
    else:
        print(lst1[29 - x], end=' ')
print('\n\n')

for x in lst2:
    print(x, end=' ')
print()

for x in range(len(lst2)):
    if x % 20 < 9:
        print(lst2[x], end=' ')
    elif x % 20 == 9:
        print(lst2[x])
    elif x % 20 == 19:
        print(lst2[29 - x])
    else:
        print(lst2[29 - x], end=' ')