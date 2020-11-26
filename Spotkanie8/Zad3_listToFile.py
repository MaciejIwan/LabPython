def write():
    list = ["MAMA", "TATA", "STUDENT", "UCZELNIA"]
    with open("Zad3_Output.txt", 'w') as open_file:
        for element in list:
            open_file.write(element)
            open_file.write('\n')
if __name__ == "__main__":
    write()