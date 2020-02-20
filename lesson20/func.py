# def hello():
#     print('hello')

def getName():
    name = input('your name> ')
    return name


def hello(name):
    print('hello,' + name)

def loop(name):
    for index in name:
        print(index)


#hello(getName())
loop(getName())

#getName()

