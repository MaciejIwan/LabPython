with open('LiczbyPierwsze.txt', 'r') as file1:
    with open('zbior2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

for elements in same:
    print(elements, end="")