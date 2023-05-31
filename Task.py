# surname = ["Петров","Иванов","Сергеев","Поляков","Кулик","Зверев","Максимов"]
# name = ["Пётр","Иван","Сергей","Валерий","Роман","Владислав","Максим"]
# phone_Num = ["891","892","893","894","895","896","897"]
# discription = ["рабочий","домашний","рабочий","личный","личный","домашний","домашний"]

def get_Info():
    info = []
    surname = input("Введите фамилию: ")
    info.append(surname)
    name = input("Введите имя: ")
    info.append(name)
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
    description = input("Введите описание: ")
    info.append(description)
    return info

def writing_Txt_File(info):
    file = "Phonebook.txt"
    with open(file, "a", encoding = "utf-8") as data:
        data.write(
            f"Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n")
        
