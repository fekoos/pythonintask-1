# Задача 3. Вариант 9
# Напишите программу, которая выводит имя "Доменико Теотокопули" и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Лагвилава А.
# 05.04.2017

name = ("Доменико Теотокопули")
print(name)
print("Это великий испанский живописец, архитектор и скульптор.")
nikname = input("\nПод каким псевдонимом этот человек вошел в историю? Ваш ответ: ")
if nikname == "Эль Греко":
    print("\nПравильно!", name, " - ", nikname)
else:
    print("\nНеправильный ответ")
input("\nНажмите Enter, чтобы выйти")
