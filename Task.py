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

def view():
    print(from_File("Phonebook.txt"))

continue_Action = "yes"

while continue_Action == "yes":
    type_Of_Action = input("Если хотите просмотреть список всех контактов введите\t'read'\nЕсли хотите дабавить новый контакт введите\t'write'\nЕсли хотите найти контакт введите\t'search'\n")
    if type_Of_Action == "write":
        record_info()
    if type_Of_Action == "read":
        view()
    continue_Action = input("Для продолжения введите 'yes'\nЧтобы закончить введите, любой другой символ\n")