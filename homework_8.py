#Генератор паролей
import random
import string
passwords = {}

def show_menu ():
    print ("1 - Показать пароли.") 
    print ("2 - Добавить пароль.")
    print ("3 - Удалить пароль.")
    print ("4 - Обновить пароль.")
    print ("5 - Выход.")
    sel_menu = int(input("Введите цифру пункта меню: "))

    match sel_menu:
        case 1: 
            print("# ПОКАЗАТЬ ПАРОЛИ")
            show_passwords ()
        case 2: 
            print("# ДОБАВЛЕНИЕ ПАРОЛЯ")
            add_password ()
        case 3: 
            print("# УДАЛЕНИЕ ПАРОЛЯ")
            delete_password ()
        case 4: 
            print("# ОБНОВЛЕНИЕ ПАРОЛЯ")
        case _:
            exit()

def gen_pass (lengts:int):
    all_chars = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    password_chars: list[str] = []
    #user_input = input("Введите длину пароля: ")
    #lengts = lengts = int(user_input) if user_input.isdigit() else 7

    while len(password_chars) < lengts:
        password_chars.append(random.choice(all_chars))
        
    return "".join(password_chars) 

def add_password ():
    user_domain = input("Введите логин: ")  #Запрашиваем у пользователя домен и пароль.
    user_password = input("Введите пароль или оставьте пустым для автогенерации: \n")   #Если пароль пустой, генерируем его автоматически.
    if user_password == "":
        user_password = gen_pass (8)

    if user_domain in passwords:
        print("Этот логин уже существует: \n\n")
        show_menu()
    else:
        passwords[user_domain] = user_password #Сохраняем домен и пароль в словарь.
        print("Логин и пароль записан! \n\n" )
        show_menu()

def show_passwords ():
    print(passwords)
    show_menu()

def delete_password ():
    need_del_pass = input("Введите логин для удаления: ")
    if need_del_pass in passwords:
        passwords.pop (need_del_pass)
        print("Логин и пароль удалены! \n\n" )
        show_menu()
    else:
        print("Таких логина и пароля нет! \n\n" )
        show_menu()


show_menu()



