from random import randint

def rand():
    return randint(0,50)



numbers = []
for index in range(0,   10):
    numbers.append(rand())
    print(numbers[index])

# print('index 3 = ', numbers[3])

def avarage(numbers):
    summa = 0
    for index in numbers:
        summa += index
    # print(summa/len(numbers))
    return summa/len(numbers)
print('Avarage = ',avarage(numbers))


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


# summ3(numbers)
avarage(numbers)

