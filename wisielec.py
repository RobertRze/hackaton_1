import random


def check_letter(mask_word, word, tries_number):
    num = 0
    while num == 0:
        letter = input(f'Liczba prób {tries_number}. Podaj literę: ')
        num = word.count(letter)
        if num > 0:
            print("Trafione!")
            return print_word(mask_word, word, letter)
        else:
            print('Nie trafione, spróbuj jeszcze raz')
            return mask_word


def print_word(mask_word, word, letter):
    i = 0
    for i in range(len(word)):
        if word[i] == letter:
            mask_word[i] = letter
    return mask_word


def show_word(mask_word):
    format_word = ''
    for i in range(len(mask_word)):
        format_word += mask_word[i]
        i += 1
    return format_word

def check_word(word, mask_word):
    user_word = input("Podaj słowo: ")
    if word == user_word:
        return word
    else:
        print("Pudło")
        return mask_word

def guess_word(mask_word, word, tries_number):
    guess_word_choice = 'x'
    while guess_word_choice != 't' or guess_word_choice != 'n':
        guess_word_choice = input("Chcesz spóbować odgadąć słowo (t - koszuje 2 próby)? (t/n): ")
        if guess_word_choice == 't':
            return check_word(word, mask_word), tries_number - 2
        elif guess_word_choice == 'n':
            return mask_word, tries_number
        else:
            print('Niepoprawna wartość')


def fill_word():
    word_list = ['krowa', 'kot', 'pies', 'kaczka']
    word = word_list[random.randint(0, len(word_list) - 1)]
    #print(word)
    word_size = len(word)
    mask_word = len(word) * '-'
    print(mask_word)
    mask_word = list(mask_word)
    i = 0
    while mask_word.count('-') > 0 and i < 10:
        tries_number = 10 - i
        check_letter(mask_word, word, tries_number)
        print(show_word(mask_word))
        guest_word_result = guess_word(mask_word, word, tries_number)
        mask_word = guest_word_result[0]
        i = 10 - guest_word_result[1]
        #i = 10 - guess_word(mask_word, word, tries_number)[1]
        print(show_word(mask_word))
        i += 1
    return show_word(mask_word), word


def main():
    fill_word_result = fill_word()
    count = fill_word_result[0].count('-')
    word = fill_word_result[1]
    if count > 0:
        print(f'Przegrałeś. Słowo do odgadnięcia: {word}')
    else:
        print('Wygłałeś')

main()