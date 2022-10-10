name = input("Название файла: ")
while(True):
    with open(name + ".txt", "a") as file:
        string = input("введите строку: ")
        if(len(string) < 3 or string.isalpha() == False):
            print("Некорректный ввод")
            continue
        else:
            file.write("\n" + string)
            break
