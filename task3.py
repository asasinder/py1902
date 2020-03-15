import random

def rand():
    a = random.randint(0,50)
    return a

print(rand())

c = [rand() for i in range(int(input()))]
# c = [rand() for i in range(a)]
print (c)



#  rand()
# print(a)
print(sum(c),len(c))