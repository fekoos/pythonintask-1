# Задача 5. Вариант 22.
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из двух сооснователей компании Google.
# Kiknadze G.V.
# 2017-02-28

import random

names=("Сергей Михайлович Брин, Ларри Пейдж")
print("Случайное имя поросенка: " + names[random.randint(0, 1)])