# Задача 3. Вариант 14.
# Напишите программу, которая выводит имя "Доменико Теотокопули", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Русаков В.А.
# 15.04.2017

name = "Вильгельм Аполлинарий Костровицкий"
print("Герой нашей сегоднящней программы - " + name)
alias = input("Под каким же именем мы знаем этого человека? Ваш ответ: ")

print("Все верно: " + name + " - " + alias)

input("\n\nНажмите Enter для выхода.")