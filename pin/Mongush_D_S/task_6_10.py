# Задача 6. Вариант 10.
# Mongush D.S.

# 05.04.17

#Импортируем модуль рандом из библиотеки, чтобы можно было пользоваться его функционалом
import random

#создаем кортеж
kortej = ("Германия", "Австро-венгрия", "Италия")
#присваиваем переменной word случайно выбранное значение из значений kortej
word = random.choice(kortej)
#Объясняем правила игры
print("Компьютер загадал одно из значений: `Германия`, `Австро-венгрия`, `Италия`")
#присваиваем переменной vvod значение введенное с клавиатуры
vvod = input("Ваше слово:")
#предлагаем ввести слово до тех пор, пока случайно выбранное не совпадет с введенным
while vvod != word:
    vvod = input("Ваше слово:")
#выводим строку
print("Правильно!")
#Ждем нажатия Enter для выхода
input("\n\nНажмите Enter, чтобы выйти.")

