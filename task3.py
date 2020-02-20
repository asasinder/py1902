import random

def rand():
    a = random.randint(0,50)
    return a

#print(rand())
c = [rand() for i in range(int(input()))]
print (c)
# rand(a)
# print(a)

print(sum(c),len(c))