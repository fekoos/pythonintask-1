# Задача 8. Вариант 9.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен
#его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток
#узнать, есть ли какая-либо буква в слове, причем программа может отвечать только
#"Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.
#
# Казазаев Дмитрий Евгеньевич
# 23.04.2017

import random


WORDS=['собака', 'платина', 'кулич', 'антисептик']
i=1
guess = 'h'

word = random.choice(WORDS)
print(
"""
Добро пожаловать в игру 'Угадай слово!
Вы должны угадать слово, загаданное компьютером.
(Для выхода нажмите Enter, не вводя своей версии.)
"""
)
print('Ваше слово состоит из ',len(word), 'букв.' '\nУ Вас пять попыток узнать, есть ли какая-либо буква в слове. \n("Да" - буква присутствует. "Нет" - буква отсутствует)')
while i != 6 :
    print('\nПопытка №', i)
    symb = input('Введите букву :')
    if symb == "" :
        break
    elif word.find(symb[0]) > -1 :
        print('Да')
    else :
        print('Нет')
    i+=1
if symb != "" :
    while guess != word or guess != "" :
        guess = input('Ваш ответ:')
        if guess == word :
            print('Поздравляю, Вы отгадали слово!')
            break
        else :
            print('Увы, Вы не отгадали слово.')
    
input("\nНажмите Enter для выхода.")
