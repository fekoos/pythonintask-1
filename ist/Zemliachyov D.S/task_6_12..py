
import random

answer = input('Назовите один из соборов Московского кремля.'
     +'\nПопробуй отгадать:'
	 +'\n1 - Колокольня Ивана Великого, 2 - Успенский собор, 3 - Благовещенский собор, 4 - Архангельский собор, 5 - Храм Положения ризы Божией Матери во Влахерне, 6 - Патриарший дворец и собор Двенадцати апостолов, 7 - Верхоспасский собор, 8 - Церковь Рождества Богородицы на Сенях'
      +'\nТвой ответ: ')

n = random.randint(1, 2)
if(int(answer) == n):
    result = '\nВерно'
else:
    result = '\nНе верно'
print(result)
input('\n\nНажмите Enter для выхода.')