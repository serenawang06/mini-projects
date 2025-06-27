import random

wordbank = ['apple', 'banana', 'cucumber', 'dropship', 'elephant']
word = random.choice(wordbank)
hangman = ['' ,'head', 'body', 'right arm', 'left arm', 'right leg', 'left leg']
maxWrong = len(hangman)
wrong = 0
guessed = []
wordDash = ('-') * len(word)

while wrong < maxWrong and wordDash != word:
    print('')
    print(hangman[wrong])
    print('word: ' + wordDash)
    print('Guessed: ' + str(guessed))
    
    guess = input('Guess a letter: ').lower()

    while guess in guessed:
        print('You already guessed it, try again')
        print('')
        guess = input('Guess a letter: ').lower()

    guessed.append(guess)

    if guess in word:
        print(guess + ' is in the word')
        print('')
    
        new = ''
    
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += wordDash[i]
    
        wordDash = new
    else:
        print('try again')
        wrong += 1
    
if wrong == maxWrong:
    print('the word is ' + word)
    print('better luck next time')
else:
    print('the word is ' + word)
    print('congrats you got it')    