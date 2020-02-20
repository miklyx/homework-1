"""

Домашнее задание №1

Цикл while: ask_user

  Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
4. При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет "Пока!" 

*********************   DONE  ************************************

"""


def ask_user():
  s = ""
  while s != "Хорошо":
    s = input("Как дела? ")
  
def get_answer(a):
  try:
    while a != "Пока!":
      ask_user(a)
      # return "Сам ты" + s
  except TypeError:
    print("Пада пада пам, пиу!")

    
if __name__ == "__main__":
    # ask_user()
    get_answer(ask_user())
