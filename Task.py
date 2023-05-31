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
        
def from_File(file):
    with open(file, "r", encoding="utf-8") as data:
        dictionary = data.read()
    return dictionary

def view():
    print(from_File("Phonebook.txt"))


def record_info():
    info = get_Info()
    writing_Txt_File(info)

def choice():
    flag = input(
        "Для продолжения работы нажмите \"да\", или любой символ для завершения работы...")
    while (flag.lower() == "да"):
        path = "Phonebook.csv"
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Введите \'да\', если хотите записать новые данные, и любой другой символ, если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == 'да':
            record_info()
        else:
            view()
        flag = input(
            'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    print('Программа завершена.')

info = get_Info()
writing_Txt_File(info)
search = input("\nПоиск: ")
from_File(search)