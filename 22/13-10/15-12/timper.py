

def farenheut(celsium):

    farenheut= (5/9) * celsium + 32
    return farenheut



def celsium(celsium):
    celsium = 9/5 * celsium - 32
    return celsium


def kelvin(celsium):
    kelvin = celsium + 273
    return kelvin

celsium = int(input('ведите C :'))
 farenheut = int(input('ведите F :'))
 kelvin = int(input('ведите K :'))

print(farenheut(celsium))
print(celsium(farenheut))
print(kelvin(celsium))

'''
def farenheut(celsium):
    res1 = (5/9)*(celsium + 32)
    print( res1)
def celsium(farenheut):
    res2 = (5/9)*(farenheum - 32)
    print(res2)
def kelvin(celsium):
    res3 = (celsium + 273,15)
    print(res3)
'''