"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break

************************  DONE  *******************************

    
"""

def ask_user():
  
    vocab={"Как дела": "Хорошо!", "Что делаешь?": "Программирую","Штурман, прибор":"Пятнадцать","Что пятнадцать?":"А что прибор?"}
    s = ""
    while s != "exit":
      try:
        s = input("Введите вопрос: ")
        print(ask_user_dict(vocab,s))
      except KeyboardInterrupt:
        print("Пока!")
        break
def ask_user_dict(voc,st):
  for i in voc.keys():
    if i == st:
      return voc.get(i)
    else:
      print("Вопрос отсутствует в словаре")    

if __name__ == "__main__":
    ask_user()
