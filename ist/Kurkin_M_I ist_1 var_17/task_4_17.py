#Задача 4. Вариант 17.
#Напишите программу, которая выводит	имя, под которым скрывается Грета Густафсон.	
#Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы	рождения и смерти (если	человек	умер), 
#вычислить возраст на	данный	момент	(или	момент	смерти).	Для	хранения	всех необходимых	данных	требуется	использовать	переменные.	
#После	вывода информации	программа	должна	дожидаться	пока	пользователь	нажмет	Enter	для выхода.

#Kurkin M. I.
#19.04.2017
Name = "Грета Гарбо"

print ("Грета Густафсон более известна, как", Name)

Interests = " шведская и американская актриса."

print ("Область интересов: ", Interests)

PlaceOfBirth = "Стокгольм, Швеция"

print ("Место рождения: ", PlaceOfBirth)

DateOfBirth = ("1905")

DateOfBirth = int(DateOfBirth)

print ("Год рождения: ", DateOfBirth)

DateOfDeath = ("1990")

DateOfDeath = int(DateOfDeath)

print ("Год смерти: ", DateOfDeath)

Age = (DateOfDeath - DateOfBirth)

print ("На момент смерти" ,Name, "было", Age, " лет.")

input ("Для выхода из программы нажмите клавишу <Enter>.")