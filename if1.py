"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

****************  DONE   ***************************


"""

def main():
  age = int(input("Input age: "))
  ocp = occupation(age)
  print(ocp)

def occupation(ag):
   if ag < 7:
     return "detsad"
   elif ag < 17:
     return "school"
   elif ag < 21:
     return "university"
   else:
     return "work"
  

if __name__ == "__main__":
    main()
