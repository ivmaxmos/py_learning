
""" Требования:
Для дней 1–5 выведите название дня и строку "Будний день".
Для дней 6 и 7 выведите название дня и строку "Выходной день".
Если введено число вне диапазона 1–7, выведите только "Некорректный день". """

day_number = int(input("Введите номер дня от 1 до 7: "))

match day_number:
    case 1:
        day_name = "Понедельник"
    case 2:
        day_name = "Вторник"
    case 3:
        day_name = "Среда"
    case 4:
        day_name = "Четверг"
    case 5:
        day_name = "Пятница"
    case 6:
        day_name = "Суббота"
    case 7:
        day_name = "Воскресенье"
    case _:
        day_name = None

if day_name == None: 
    print("Некорректный день")
else:
    status = "Выходной день" if day_number >= 6 else "Будний день"
    print(day_name)
    print(status)
    

