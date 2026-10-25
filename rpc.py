#Игра камень - ножницы - бумага
#Мы запрашиваем у пользователя, сколько раундов он хочет сыграть.
#Пользователь делает свой выбор из "Камень", "Ножницы", "Бумага".
#Компьютер случайным образом выбирает свой вариант с использованием библиотеки random.
#Мы сравниваем выборы и определяем победителя раунда.
#Ведется подсчет очков для пользователя и компьютера.

import random

choises = ["камень", "ножницы", "бумага"]
rounds = int(input("Введите количество раундов: "))
user_star: int = 0
pc_star: int = 0

for round in range(rounds):
    pc_choise = (random.choice(choises))
    user_choise = input("Введите камень, ножницы или бумага: ").lower().strip()
    if user_choise == pc_choise: 
        print(f"Компьютер тоже выбрал: {pc_choise} -> 0 баллов") 
        continue
    if user_choise == "камень" and pc_choise == "ножницы": print(f"Компьютер выбрал: {pc_choise} -> Балл пользователю"); user_star += 1
    if user_choise == "камень" and pc_choise == "бумага": print(f"Компьютер выбрал: {pc_choise} -> Балл компьютеру"); pc_star += 1
    if user_choise == "ножницы" and pc_choise == "бумага": print(f"Компьютер выбрал: {pc_choise} -> Балл пользователю"); user_star += 1
    if user_choise == "ножницы" and pc_choise == "камень": print(f"Компьютер выбрал: {pc_choise} -> Балл компьютеру"); pc_star += 1
    if user_choise == "бумага" and pc_choise == "ножницы": print(f"Компьютер выбрал: {pc_choise} -> Балл компьютеру"); pc_star += 1
    if user_choise == "бумага" and pc_choise == "камень": print(f"Компьютер выбрал: {pc_choise} -> Балл пользователю"); user_star += 1
    
if user_star > pc_star:
    print(f"Вы выиграли, у вас {user_star} а у компа {pc_star} балл(а)")
elif user_star < pc_star:
    print(f"Комп выиграл, у него {pc_star} а у вас {user_star} балл(а)")
else:
    print("Ничья, победила дружба")



