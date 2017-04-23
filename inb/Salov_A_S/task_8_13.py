# Задача 8. Вариант 13.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Salov A. S.
# 22.03.2017

print(
"""
\t\t\t   Добро пожаловать в игру!
\t\t\tСоставь слово из букв и выиграй!
"""
)
import random
def help_func(a):
	if a=='питон':
		print('Очень знакомый язык...')
	if a=='гравицапа':
		print('Устройство, с которым в любую точку вселенной за 5 секунд')
	if a=='гравитация':
		print('Взаимодействие между всеми материальными телами')
	if a=='орбита':
		print('Траектория небесного тела в гравитационном поле более массивного объекта')
	if a=='карлик':
		print('Крайне не высокий человек')
	if a=='спектр':
		print('Распределение значений физической величины')
	if a=='квазар':
		print('Один из самых ярких астрономических объектов в видимой Вселенной.')
		
och=0;ochp=0;koef=0;n=0;flag1=True;flag2=False
def och_func(b):
	global koef
	global ochp
	global och
	global n
	if b==1:
		koef=50
	if b==0:
		n+=1
		ochp=100-koef
		och+=ochp
		koef=0
		print('Вы заработали',ochp,'очков')
		print('Всего у Вас  ',och, 'очков')
		
while 0!=1:
	WORDS = ("питон", "гравицапа", "гравитация", "орбита", "карлик", "спектр", "квазар")
	word = random.choice(WORDS)
	correct = word
	jumble =""
	while word:
		position = random.randrange(len(word))
		jumble += word[position]
		word = word[:position] + word[(position + 1):]
	print("Загаданное слово:", jumble,'.\nВедите "помощь" для получения подсказки')
	guess = input("\nВаш ответ: ")
	while 0!=1:	
		while guess == "помощь":
			help_func(correct)
			och_func(1)
			guess = input("\nВаш вариант: ")
		while guess != correct and guess != "помощь":
			print("Ответ \"", guess, "\" не верен")
			print("\nЗагаданное слово:", jumble,'.\nВедите "помощь" для получения подсказки')
			guess = input("\nВаш вариант: ")
		if guess == correct:
			och_func(0)
			print("""
			!!!!!!!!!!!
			!!!Верно!!!
			!!!!!!!!!!!
			""")
			g=input('Сыграть ещё? да / нет\n')
			while 1!=0:
				if g=='да':
					break
				elif g=='нет':
					flag2=True
					print('Спасибо за игру!')
					if (5<=n<=20 or 5<=n%10<=10):
						otv='ответов'
					elif 2<=n%10<=4:
						otv='ответа'
					elif n%10==1:
						otv='ответ'
					print('За',n,'правильных',otv,'вы набрали',och,'очков')
					input()
					break
				else:
					g=input('Сыграть ещё? да/нет\n')
					continue
		if flag1:
			break
	if flag2:
		break