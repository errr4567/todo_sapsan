#импорт библии


TOKEN = ""

HELP = """
help - вывод списка команд
add - добавить
show - показать все задачи
done - выполнены
"""

todo = {}

print("Привет, Введите команду Help для ввода списка команд")

while True:
  UserAnswer = input("Введите команду:\n")
  

  if UserAnswer == "":
   print('Работает')
  elif UserAnswer == "help":
   print('Работает')
  elif UserAnswer == "show":
   print('Работает')
  elif UserAnswer == "done":
   print('Работает')
  elif UserAnswer == "exit":
   print('Работает') 
  else:
    print("error.нет такой команды")
    print("Введите Help для вывода списка команд")

   
