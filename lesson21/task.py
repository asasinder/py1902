# запрос имени и возрат его
def getName():
    name = input('your name> ')
    print('Hi,' + name)
    return name

# запрос возраста и возрат его
def age():
    age = input('how old are you > ')
    return age


# проверка имени и возраста
def check(name,age):
    a = len(name) * age
    summ = len(name) + age
    print(a)
    if (a > 30 and a < 40):
        for index in name:
            print(index)
    elif a > 40:
        print(name*3)
    elif summ < 20:
        print(name.upper())
    else:
        for index in range(0,summ,4):
            print(index)

        print(len(name) + age)

# for index in range(0,10,4)
#     print(index)


# вызов функции
a = int(age())
n = getName()
check(n,a)