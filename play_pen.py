# playing around
from django.forms import Input

vowels_string = 'aeiouy'
input_to_scramble = input('Scramble: ')


def scramble_the_vowels(alpha, sent):
    # coded_message = 'coded message; '
    for vowel in alpha:
        print (vowel)
        for letter in sent:
            if vowel == letter:
                print('yes')
            else:
                print('no')
            #     coded_message += letter
            #     print(coded_message)

scramble_the_vowels(vowels_string, input_to_scramble)

input_to_decode = input('Decoded: ')


# getting there... kinda
input_to_scramble = input('Scramble: ')


def scramble_the_vowels(sent):
    
    vowel_string = ['a', 'e', 'i', 'o', 'u', 'y']
    
    for vowel in vowel_string:
        vowel_index = vowel_string.index(vowel)
        print(vowel + str(vowel_index))
        
    empty_string = ''
    
    for letter in sent:
    
        if letter in vowel_string:
            print(letter)
        elif letter == ' ':
            print(' ')
        else:
            print(letter)


scramble_the_vowels(input_to_scramble)




scramble = input('Scramble: ')
def use_scrable(clean_text):
    vowel_1 = 'a'
    vowel_2 = 'e'
    vowel_3 = 'i'
    vowel_4 = 'o'
    vowel_5 = 'u'
    new_word = ''
    for letters in clean_text:
        if letters == 'a':
            new_word += vowel_2
        elif letters == 'e':
            new_word += vowel_3
        elif letters == 'i':
            new_word += vowel_4
        elif letters == 'o':
            new_word += vowel_5
        elif letters == 'u':
            new_word += vowel_1
        else:
            new_word += letters
    print(new_word)
use_scrable(scramble)

decode = input('Descramble: ')
def use_decode(code_word):
    vowel_1 = 'a'
    vowel_2 = 'e'
    vowel_3 = 'i'
    vowel_4 = 'o'
    vowel_5 = 'u'
    new_word = ''
    for letters in code_word:
        if letters == 'i':
            new_word += vowel_2
        elif letters == 'o':
            new_word += vowel_3
        elif letters == 'u':
            new_word += vowel_4
        elif letters == 'a':
            new_word += vowel_5
        elif letters == 'e':
            new_word += vowel_1
        else:
            new_word += letters
    print(new_word)
use_decode(decode)