"""
1.Пройдите по списку в цикле ["Вася","Маша","Петя","Валера","Саша","Даша"]
пока не встретиться имя Валера. Когда найдете напишите "Валера нашелся". Подсказка : используйте метод lost.pop()
2. Перепишите предыдущий пример в виде функцции find_person(name), которая ищет имя в списке.
3. Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
4. При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет "Пока!"

"""


def main():
  test_findname()
  
def input_list():
  lst = []
  c = input("1 - список по-умолчанию, 2 - свой список: ")
  if c == '1':
    lst=["Вася","Маша","Петя","Валера","Саша","Даша"]
    return lst
  else:
    cnt = input("Введите количество записей :")
    for i in range(int(cnt)):
      lst.append(input("Имя: "))
    return lst

def find_person(lst,name):  
  i = 0
  while True:
    if lst[i] == name:
      s = name+" нашелся"
      break
    else:
      i = i+1
  return s
def test_findname():
  name_l = input_list()
  name_f = input("Кого ищем? ")
  print(find_person(name_l,name_f))

main()