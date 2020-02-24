"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.

**********************   DONE   **************************************

"""

def main():
  f = input("1 - middle score school, 2 - middle score of classes : ")
  if f == '1':
    print(midschool(voclist()))
  else:
    for i in midclasses(voclist()):
      print("class : ",i["school_class"], "midscore: ",i["midscore"])

def voclist():  
  school = [{'school_class': '4a', 'scores': [3,4,2,5,2]},{'school_class': '4b', 'scores': [5,4,4,5,2]},{'school_class': '4c', 'scores': [2,3,2,1,2]}]
  return school

# переделай данную функцию с использованием функций, которые я прописала в функции midclasses
def midschool(lst):
  cnt=0
  #переменные не называют уже зарезервированными словами sum можно заменить на summa
  sum=0
  for i in lst:
    sc=i["scores"]
    for j in sc: 
      cnt = cnt + 1
      sum = sum + j
  return round(sum/cnt,2) 

def midclasses(lst):
  # cntc=0
  # sumc=0
  lst2=[]
  for i in lst:
    scc=i["scores"]
    # for j in scc: 
    #   cntc = cntc + 1
    #   sumc = sumc + j
    # i["midscore"]=round(sumc/cntc,2)
    i['midscore'] = sum(scc)/len(scc)
    # cntc=0
    # sumc=0
    lst2.append(i)
  return(lst2)

if __name__ == "__main__":
    main()
