"""Iterating through arrays"""


def printLineBreaker():
    for counter in range(0, 50):
        print('*', end='')
    print('')


names = ['Ragini', 'Karthik', 'Ved']
for name in names:
    print(name)
printLineBreaker()

for name in names:
    if name == 'Ved':
        print('hello ' + name)
printLineBreaker()

for i in range(0, 10):
    print('value is ' + str(i))

printLineBreaker()

i = 1
while i < 50:
    if i % 2 == 0:
        print('Even number :' + str(i))
    i = i + 1


