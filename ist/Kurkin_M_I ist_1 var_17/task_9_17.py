#Задача 9. Вариант 17.
#Напишите	программу,	которая	будет	сообщать	род	деятельности	и	псевдоним	под которым	скрывается	Алексей	Максимович	Пешков.	
#После	вывода	информации программа	должна	дожидаться	пока	пользователь	нажмет	Enter	для	выхода.

#Kurkin M. I.
#19.04.2017
import random

wordslist = ( "прогресс", "разряд", "эпопея", "корпорация", "рефлексия", "протест", "узурпация","диэтиламид",)

wordslist += ("проекция", "конструктор" , "метрика" , "ортогональность",)

word = random.choice(wordslist)

print('Я загадал одно сложное слово. Ты должен его угодать.')

print("В нём", len(word), "букв")

print("Я дам тебе возможность очутиться на 'Поле чудес': выбери пять букв, а я скажу есть ли в том слове эти буквы")

for i in range(5):

	tring=input("Вводи по одной. Ожидаю ввод.\n")

	if tring in word:

		print("Да")

	else:

		print("Нет")

print("Теперь угадай слово")

answer=" "

while answer!=word and  answer!="":

	answer= input("\n")

if answer==word:

	print("Замечательно, вы угадали")

print("FINISH")