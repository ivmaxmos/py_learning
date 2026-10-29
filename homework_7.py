# ТАБЛИЦА УМНОЖЕНИЯ (вложенные циклы)
# a: int = 1
# b: int = 1

# for b in range(1, 11):
#     for a in range(1, 11):
#         print(f"{a*b:4}", end="")
#         a += 1 
#     print ()
#     b += 1

from typing import Literal

def calculate (a: float, b: float, operator: Literal["/", "*", "-", "+"]):
    """ Математическая операция над 2 числами """
    match operator:
        case "/": 
            if b == 0: return "Ошибка, дел на 0"
            else: return a / b
        case "*": 
            return a * b
        case "-": 
            return a - b
        case "+": 
            return a + b
        case _:
            return "Ошибка"

print(calculate (11, 0, "/"))


#Генератор паролей
import random
import string

def gen_pass (lenght:int = 4):
    password = ""
    all_chars = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    password_chars: list[str] = []
    user_input = input("Введите длину пароля: ")
    lengts = lengts = int(user_input) if user_input.isdigit() else 4

    while len(password_chars) < lengts:
        password_chars.append(random.choice(all_chars))
        
    return "".join(password_chars) 


print(gen_pass ())

