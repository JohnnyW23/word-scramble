def title():
    print(f'''\033[36m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
{'SCRAMBLYTHON v1.0'.center(43)}
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[m
''')


def generateWord(min):
    from words import word_list
    from random import choice

    while True:
        secret_word = choice(word_list).upper()
        if len(secret_word) >= min: break

    index = []

    for i, _ in enumerate(secret_word): index.append(i)

    scrambler = []

    for _ in secret_word:
        x = choice(index)
        scrambler.append(secret_word[x])
        index.remove(x)
    
    scrambled = ' '.join(scrambler)

    return secret_word, scrambled


def game(secret_word, scrambled, v, d):
    from time import sleep

    print('Try to guess the word!')
    sleep(1)
    print(f'''
\033[33m{scrambled}\033[m
''')
    answer = input('The word is: ').upper().strip()
    print()
    if answer == secret_word:
        print('\033[32mCongratulations, you found the word!\033[m')
        v += 1
        d += 0
        return v, d
    else:
        print(f"I'm sorry! The word is \033[33m{secret_word}\033[m.")
        v += 0
        d += 1
        return v, d


def playAgain():
    from time import sleep

    sleep(1)
    while True:
        answer = input('''
Do you want to play again? \033[33m[Y/N]\033[m: ''').upper().strip()
        print('''
===============================================
''')
        sleep(0.5)
        if answer == 'N': return False
        elif answer == 'Y': return True
        else: print('\033[31mINVALID ENTRY!\033[m')


def exit(c, v, d):
    from time import sleep
    time = 'time'
    if c > 1: time = 'times'
    print(f'\033[35mYou played Scramblython {c} {time}!')
    sleep(0.5)
    print(f'Victories: {v}')
    sleep(0.5)
    print(f'Defeats: {d}')
    sleep(0.5)
    print('Thank you and come back :)\033[m')
    print()
