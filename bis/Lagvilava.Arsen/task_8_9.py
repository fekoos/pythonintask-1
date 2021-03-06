# Задача 8. Вариант 9
# Доработайте игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Лагвилава А.
# 08.04.2017

import random
WORDS = ("программирование", "информатика", "питон", "компьютер", "клавиатура", "кодирование")
word = random.choice(WORDS)
correct = word
help = correct
jumble = ""
count = 0
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(
"""
                 Добро пожаловать в игру "Анаграммы"!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
"""
)
print("Вот анаграмма: ", jumble)
print("Для вывода подсказки нажми Enter")
guess = input("\nПопробуйте отгадать исходной слово: ")
points = 20

while 1 > 0:
    if guess == "":
        points = points - 1
        print (help[0])
        help = help[1:]
        guess = input("\nПопробуйте отгадать исходной слово: ")
    elif guess != correct:
        print("Неверно. Попробуй еще раз")
        guess = input("\nПопробуйте отгадать исходной слово: ")
    elif guess == correct:
        print("Молодец! Ты отгадал!")
        print("Количество очков: ", points)
        print("Спасибо за игру!")
        break
input("\nНажмите Enter, чтобы выйти")

