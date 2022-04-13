import webbrowser
import random

from colorama import Fore, Back, Style

# 2 char alpha combo
def print_Alphabet(option):
    results = {}
    count = 0
    alphabet = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z'
    }
    if option == "Yes":
        for key, value in alphabet.items():
            for key1, value1 in alphabet.items():
                count = count + 1
                results.update({count: value+value1})
    else:
        print(option, "No Print Required")

    return results

# 4 digits number combo
def print_Numbers(option):

    results = {}
    count = 0
    numbers = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9
    }
    if option == "Yes":
        for key, value in numbers.items():
            for key1, value1 in numbers.items():
                for key2, value2 in numbers.items():
                    for key3, value3 in numbers.items():
                        count = count + 1
                        result_String = str(value)
                        result_String1 = str(value1)
                        result_String2 = str(value2)
                        result_String3 = str(value3)
                        four_digit_int = (result_String + result_String1 + result_String2 + result_String3)
                        results.update({count: four_digit_int})

    else:
        print(option, "No Print Required")

    return results

#combine alpha and number combo
def print_Search(letter_Combo, number_Combo):

    results = {}
    count = 0

    for letter_Combo_Key, letter_Value in letter_Combo.items():
        for number_Combo_Key, number_Value in number_Combo.items():
            #print(letter_Value + number_Value)
            count = count + 1
            results.update({count: letter_Value + number_Value})

    return results

#return the finished combo
def get_List():
    letter_Combo = print_Alphabet('Yes')
    number_Combo = print_Numbers('Yes')
    search_Links = print_Search(letter_Combo, number_Combo)
    return search_Links

