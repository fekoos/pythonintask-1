#Задача 8. Вариант 8.
#1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
#так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право 
#на подсказку в том случае, если у него нет никаких предположений. Разработайте
#систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
#получали больше тех, кто запросил подсказку.
#Krotkova V.D
#20.04.2017


import random

#cоздадим последовательность слов, из которых компьютер будет выбирать
WORDS = ("яблоко", "персик", "тыква", "игрушка", "свинья", "огурец")

#случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)
prompting = word[0] #подсказка первой буквы исходного слова
useofprompt = 0 #использование подсказки
#создадим переменную, с которой будет затем сопоставлена версия игрока
correct = word

#создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    
#начало игры
print(
"""
         Добро пожаловать в игру 'Анаграммы'!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
 (Для выхода нажмите Enter, не вводя своей версии.)
"""
)
print("Вот анаграмма:", jumble)
guess = input("\nДля подсказки введите 'подсказка'.\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    if guess == "подсказка":
        print('Первая буква исходного слова: ', prompting)
        useofprompt = 1
    else:
        print("К сожалению, вы не правы.")
    guess = input("Попробуйте отгадать исходное слово: ")
if guess == correct:
    print("\nДа, именно так! Вы отгадали!\n")
    if useofprompt:
        print('Вы заработали 3 балла!')
    else:
        print('Вы заработали 10 баллов!')
print("Спасибо за игру.")
input("\n\nНажмите Enter, чтобы выйти.")
