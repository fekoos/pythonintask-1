#Задача 9.Вариант 12.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен отгадать.
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли
#какая-нибудь буква в слове причем программа может отвечать только "да" и "нет". Вслед за тем игрок должен попробовать
#отгадать слово.

#Марчук А.Ю.
#11.04.2017

import random

WORDS = ('импровизация', 'индустриализация', 'энциклопедия', 'кошка', 'нос', 'шарф')
word = random.choice(WORDS)
length=len(word)


#Начало игры
print(
"""
Добропожаловать в игру "Отгадай слово". Надо отгадать слово, 
при этом Вы можете 5 раз спросить у компьютера, если 
там какие-либо буквы.(Для выхода нажмите Enter, не вводя своей версии)
"""
)

adviced=0

print('Длина загаданного слова: ' ,str(length))
print(' Сейчас Вы можете спросить у компьютера, есть ли в слове любая из букв алфавита:')
while adviced < 5:
	char=input('Введите букву: ')
	if char == '':
		break
	if word.find(char) > -1:
		print(' Буква' , char ,' есть в слове!')
	else:
		print('Буквы', char , 'в слове нет!')
	adviced = adviced + 1
	
	
if char != '':
	guess = input('\nПопробуйте отгадать исходное слово: ')
	
	while (guess != word or guess == '') and char != '':
		if guess == '':
			break
		print(' К сожалению, Вы не правы.')
		guess = input('Попробуйте отгадать исходное слово: ')
		
	if guess == word:
		print(' Да,именно так! Вы отгадали! Слово: ',word)
			
print('Спасибо за игру.')
input('\nНажмите Enter,чтобы выйти.')
	
	
	
	
