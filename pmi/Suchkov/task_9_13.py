# Задание 9. Вариант 10.
# Создайте игру, в которой компьютер выбирает какое-либо слово,
#а игрок должен его отгадать. Компьютер сообщает игроку,
#сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква
#в слове, причем программа может отвечать только "Да" и "Нет".
#Вслед за тем игрок должен попробовать отгадать слово..


#Сучков Р.А.

# 01.04.17

import random
a = 0
slo = ("Жизнь", "Задание", "Компьютер", "Батон", "Спорт")
rslo = random.choice(slo)

print("В слове", len(rslo), "букв, у тебя 5 попыток угадать буквы.")

while a < 5:
    a += 1
    ans = input("Угадай букву: ")
    if ans.lower() in rslo.lower():
        print("Да")
    else:
        print("Нет")

lans = input("Угадай слово: ")
if lans == rslo:
    print("Вы выиграли))")
else:
    print("Вы проиграли((")

input("\n\nНажмите Enter что бы выйти")
