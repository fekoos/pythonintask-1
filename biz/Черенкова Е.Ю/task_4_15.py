# coding: utf-8

#Задача 4. Вариант 15 

#Напишите программу, которая выводит имя, 
#под которым скрывается Анри Мари Бейль. 
#Дополнительно необходимо вывести область интересов указанной личности,
#место рождения, годы рождения и смерти (если человек умер), 
#вычислить возраст на данный момент (или момент смерти). 
#Для хранения всех необходимых данных требуется использовать переменные. 
#После вывода информации программа должна дожидаться 
#пока пользователь нажмет Enter для выхода.

#Черенкова Е.Ю.
#03.03.2017

print("Marie-Henri Beyle")
print("He is hiding under the name of Stendhal")
print("Area of interest: literature")
born=1783
dead=1842
print("He was born in",born,",in Paris.He died at",dead)
age=dead-born
print(age)
input("Press Enter")