def get_Info():
    info = []
    surname = input("Введите фамилию: ")
    info.append(surname)
    name = input("Введите имя: ")
    info.append(name)
    patronymic = input("Введите отчество: ")
    info.append(patronymic)
    phone_Num = ""
    valid = False
    while not valid:
        try:
            phone_Num = input("Введите номер телефона: ")
            if len(phone_Num) != 11:
                print("В номере телефона должно быть 11 цифр.")
            else:
                phone_Num = int(phone_Num)
                valid = True
        except:
            print("Номер телефона должен состоять только из цифр.")
    info.append(phone_Num)
    return info

def writing_Txt_File(info):
    file = "Phonebook.txt"
    with open(file, "a", encoding = "utf-8") as data:
        data.write(
            f"Фамилия: {info[0]}\nИмя: {info[1]}\nИмя: {info[2]}\nНомер телефона: {info[3]}\n\n")

def record_info():
    info = get_Info()
    writing_Txt_File(info)

def from_File(file):
    with open(file, "r", encoding="utf-8") as data:
        dictionary = data.read()
    return dictionary

def display_Result():
    print(from_File("Phonebook.txt"))

def search_Info():
    print('По какому полю выполнить поиск?')
    search_field = int(input("1 - по фамилии\n2 - по имени\n3 - по отчеству\n4 - по номеру телефона\n"))
    search_value = None
    if search_field == 1:
        search_value = input("Введите фамилию для поиска: ")
        print()
    elif search_field == 2:
        search_value = input("Введите имя для поиска: ")
        print()
    elif search_field == 3:
        search_value = input("Введите отчество для поиска: ")
        print()
    elif search_field == 4:
        search_value = input("Введите номер телефона для поиска: ")
        print()
    return search_field, search_value

continue_Action = "yes"

while continue_Action == "yes":
    type_Of_Action = int(input("1 - для добавления контакта\n2 - для просмотра всего списка контактов\n3 - для поиска контакта\n"))
    if type_Of_Action == 1:
        record_info()
    elif type_Of_Action == 2:
        display_Result()
    elif type_Of_Action == 3:
        search_Info()
    continue_Action = input("Для продолжения введите 'yes'\nЧтобы закончить введите, любой другой символ\n")