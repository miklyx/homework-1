"""
0.1 Создать список из десяти целых чисел.
Вывести на экран каждое число, увеличенное на 1.
0.2 Ввести с клавиатуры строку.
Вывести эту же строку вертикально: по одному символу на строку консоли.

******************  DONE  ************************************

"""

def main():
    k = input('1 - ten numbers, 2 - transpose string :')
    if k == '1':
      tennumbers()
    else:
      transpose()

def tennumbers():
    s=[]
    for i in range(10):
        s.append(int(input()))
    print('-----------')
    for j in s:
        print(j + 1)  

def transpose():
    st=input()
    for k in st:
        print(k)   

if __name__ == "__main__":
    main()