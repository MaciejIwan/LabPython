with open('LiczbyPierwsze.txt', 'r') as file1:
    with open('zbior2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('Liczby3.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)