# Задача 7. Вариант 7.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой
# игрок получал бы большее количество баллов за меньшее количество попыток.

# Lysenko N.A.
# 23.03.2017

import random

#Сергей Брин и Ларри Пейдж - основатели гугл

Makers = [
    "Сергей Брин",
    "Лари Пейдж"
]

pick = random.choice(Makers)
pickTry = 0

while True:
    maker = input("\nНазовите одного из двух основателей компании Google: ")

    if pick == maker:
        print("\nВы угадали, компьютер загадал: ", pick)
        print("Вы угадали с ", (pickTry + 1), " попытки и заработали ", 11 - pickTry, " очков!")
        break
    else:
        print("\nВы не угадали! Попробуйте еще раз!")
        pickTry += 1

input ('\nНажмите Enter для выхода.')
