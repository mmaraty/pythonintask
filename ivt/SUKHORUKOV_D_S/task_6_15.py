# Задача 6. Вариант 15.
# Создайте игру, в которой компьютер загадывает название одного из двенадцати
# городов, входящих в Золотое кольцо России, а игрок должен его угадать


# Сухоруков Д. С.

# 28.02.17
import random,string
cityes =  ["Переславль-Залесский", "Ростов Великий",
           "Углич","Ярославль", "Кострома", "Плёс",
           "Суздаль", "Владимир", "Юрьев-Польский",
           "Александров", "Сергиев Посад", "Тутаев"]
rightAnswer = random.choice(cityes)
print("\tПрограмма случайным образом загадывает название \n" \
      "одного из двенадцати городов, входящих в Золотое кольцо \n" \
      "России,а игрок должен угадать.\n")
answer = input("\tПопробуйте отгадать город: ")
if answer == rightAnswer:
	print("\tВсе верно!")
else:
	print("\tВы не угадали!!!\nПравильный ответ: ",rightAnswer)
input("\n\nНажмите Enter для выхода")
