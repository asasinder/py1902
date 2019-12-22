import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  O   |
      |
      |
     ===''','''
  +---+
  O   |
  |   |
      |
     ===''','''
  +---+
  O   |
 /|   |
      |
     ===''','''
  +---+
  O   |
 /|\  |
      |
     ===''','''
  +---+
  O   |
 /|\  |
 /    |
     ===''','''
  +---+
  O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''','''

  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
     ===''']

words = {'Животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь кабан змея '.split(),
        'Фрукты':'дуриан виноград банан яблоко апельсин мандарин  абрикос лимон лайм груша слива айва вишня  '.split(),
        'Цвета':'красный оранжевый желтый зеленый синий голубой фиолетовый черный белый бежевый '.split(),
        'Игры' : 'майнкрафт змейка ведьмак аэропорт-сити калибр акинатор'.split(),
        'Страны': 'тайланд египет украина германия англия литва франция италия австрия росия сша канада исландия индия китай япония норвегия швеция турция инднезия эстония финляндия монако монголия мексика '.split(),
        'Фигуры':'квадрат треугольник прямоугольник круг парелограм паралепипет трапеция ромб  '.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    #print(wordKey)
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    #print (wordDict[wordKey][wordIndex])
    return wordDict[wordKey][wordIndex]

#print(getRandomWord(words))


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Введите букву: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву')
        elif guess in alreadyGuessed:
            print('Вы уже вводили данную букву. Введите другой символ.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ')
        else:
            return guess

def playAgain():
    print('Хотите сыграть еще? (да / нет)')
    return input().lower().startswith('д')

print('H A N G M A N')

difficulty = ''

while difficulty not in 'ЛСТ':
    print('Выбирете уровень сложности: Л-легкий,С-сложный,Т-тежолый')
    difficulty = input().upper()

if difficulty == 'C':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'T':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
secretSet = secretWord
gameIsDone = False

while True:
    #print('секретное слово из наборы:'+ secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Секретное слово - "'+secretWord+'"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\n Было загадано слово:"'+secretWord+'".')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            secretSet = getRandomWord(words)
            gameIsDone = False
        else:
            break