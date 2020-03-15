# from random import randint

# def rand(startnamber, endnamber):
#     return randint(startnamber,endnamber)


# numbers = []
# for index in range(10):
#      numbers.append(rand(startnamber, endnamber))
#   print(numbers[index])

from random import randint

def rand(startnamber, endnamber):
     return randint(startnamber,endnamber)

def hello():
    name = input('Enter your name: ')
    print('hello,',name )
    age = int(input('Enter your age: '))
    print('your age is,',age )
    person = {name:age}
    return person

def transform(liste):
    first = len(liste[0])*3
    end = int(int(liste[1])*17/6)
    # print(end)
    numbers = [first, end]
    return numbers

numbers = []
# for index in range(10):
#     numbers.append((randoms[0],randoms[1]))
#     print(numbers[index])
   # return numbers

# print('index 3 = ', numbers[3])

# def avarage(numbers):
#     summa = 0
#     for index in numbers:
#         summa += index
#     # print(summa/len(numbers))
#     return summa/len(numbers)
# print('Avarage = ',avarage(numbers))


# def summ3(numbers):
#      a=sum(numbers)
#     return a
# print('Summ = ', summ3(numbers))
print(sum(numbers))

def summa2(numbers):
    summa = 0
    for index in numbers:
        if index%2 == 0:
            summa += index

    return summa
print('Summa2 = ', summa2(numbers))

def summa4(numbers):
    summa = 0
    for index in numbers:
        if index%3 == 0:
            summa += index

    return summa
print('Summa4 = ', summa4(numbers))

def summa6(numbers):
    summa = 0
    for index in numbers:
        if index%6 == 0:
            summa += index

    return summa
print('Summa6 = ', summa6(numbers))


# # summ3(numbers)
# avarage(numbers)







man = hello()
randoms = transform(man)

for index in range(10):
    numbers.append((randoms[0],randoms[1]))
    print(numbers[index])
   # return numbers


# print(man)
# print(man.values())
# print(man.keys())
# # # # namberrand = print(rand(0,10))
# # # print(rand(0,10))
# # # print(namberrand)