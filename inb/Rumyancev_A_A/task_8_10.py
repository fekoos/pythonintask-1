# Задача 8. Вариант 10.
# 1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
# так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на
# подсказку в том случае, если у него нет никаких предположений. Разработайте
# систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
# получали больше тех, кто запросил подсказку.




# Румянцев А.А.
# 16.03.2017

import random 
WORDS =("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник") 
HELPS =('змей', 'игра', 'лёгкая', 'потная', 'требование', 'стаканчик')
numb = random.randint(0,len(WORDS)-1)
word = WORDS[numb] 
print(numb)
correct = word
jumble ='"' 
points = 0
count = 0
while word:
    position = random.randrange(len(word)) 
    jumble += word[position] 
    word = word[:position] + word[(position + 1):]
print ("Добро пожаловать в игру 'Анаграммы'! /nНадо переставить буквы так. чтобы получилось осмысленное слово.")
print('Для выхода нажмите Enter. не вводя своей версии.')
print("Boт анаграмма:", jumble)
guess = input("\nПопробуйте отгадать исходное слово. Если испытываете затруднения, введите 'help': ")
while guess != correct and guess != "":
    if guess == 'help':
        print (HELPS[numb])
    else:
        print("K сожалению, вы не правы.")
        count = count+1
    if count == 6: 
        print('6 попыток, 0 очков!')
        break
    guess = input("Попробуйте отгадать исходное слово: ")
if guess == correct: 
    points = 3000 - count*500
    print("Дa. именно так! Вы отгадали!\n Ваши очки:", points) 
print("Cnacибo за игру.")
input("\n\nHaжмитe Enter. чтобы выйти.") 