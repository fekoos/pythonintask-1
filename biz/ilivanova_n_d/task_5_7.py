# Задача 5, Вариант 7 
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из семи гномов, друзей Белоснежки.

# Иливанова Н.Д.
# 20.04.2017

print('Один из гномов Белоснежки')
import random
gnom=random.randint(1,7)
if gnom == 1:
 print('Весельчак')
if gnom == 2:
 print('Ворчун')
if gnom == 3:
 print('Простак')
if gnom == 4:
 print('Соня')
if gnom == 5:
 print('Тихоня')
if gnom == 6:
 print('Умник')
if gnom == 7:
 print('Чихун')
input ('Нажмите Enter для выхода')