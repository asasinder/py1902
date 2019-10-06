from tkinter import *
import time
Name = input('пожалуста ведите имя')


name = input('пожалуста ведите логин(1235693) > ')
time.sleep(2)
porl = input('пожалуста ведите пароль(1235593) > ')
a = 1235693
b = 1235593


if name.isdigit():
    if name == '1235693':
        print('......')

else:
    time.sleep(2)
    print("ошибка 404", 'неправельный логин')


time.sleep(4)

if porl.isdigit():
    if porl == '1235593':
        print('Все хорошо открываю програму')
        time.sleep(2)
        print("Hi",Name)

else:
    time.sleep(2)
    print("ошибка 404",'неправельный пароль')


root = Tk()
root.title("Графическая программа на Python")
root.geometry("1000x600")
root.mainloop()
