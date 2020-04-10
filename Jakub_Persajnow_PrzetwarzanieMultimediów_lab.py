# -*- coding: utf-8 -*-
####################################################
### Materiały do wykładu "Przetwarzanie multimediów". 
### Laboratorium 1
### Autor: Marcin Wilczewski
### semestr zimowy 2019/2020
####################################################




##Zadanie 1
## Korzystając z wyrażeń listowych (list comprehensions) utwórz listę 100 liczb podzielnych przez 7
def create_list(how_long):
    return [7*i for i in range(how_long)]


##Zadanie 2
#Utwórz listę liczb nieparzystych. Lista dowolnej długosci.
def create_odd_numbers_list(how_many):
    return [(i*2 + 1) for i in range(how_many)]


#Zadanie 3
#Korzystając z list comprehension z napisu (string) wydobądż wszystkie cyfry

def get_numbers_from_string(string):
    return [int(i) for i in string if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]



#Zadanie 4
#Stworz ciag reprezentujacy kolejne elementy ciagu fibonaciego: 0, 1, f_[n-1]+f_[n-2]
def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_sequence(how_many_terms):
    if how_many_terms <= 0:
        print("Please enter positive integer value!")
        exit()

    for i in range(how_many_terms):
        print(fibonacci(i))

#Zadanie 5
#Utworz liste wszystkich 676 par liter alfabetu aa..zz
# alfabet = 'abcdefghijklmnopqrstuwxyz'

def create_alphabet_pairs():
    alfabet = 'abcdefghijklmnopqrstuwxyz'
    pairs_list = []

    for letter in alfabet:
        for letter2 in alfabet:
            pairs_list.append(f"{letter}{letter2}")

    return pairs_list



#Zadanie 6
#Napisz prosty generator haseł zawierającyuch znaki alfanumeryczne. Długosc hasła: min = 8, maks. 12 znaków.
#Kod powinien umożliwiać po jednym uruchomieniu uzyskanie jednego hasła w postaci listy.
#Wskazówka: hasło powinno składać się z losowo wybranych elementów wczesniej zdefiniowanego słownika (znaki alfanumeryczne).

import random

def create_password():
    alfanumeric_signs = {'znaki_alfanumeryczne': 'abcdefghijklmnopqrstuwxyz123456789'}
    len_min = 8
    len_max = 12

    random_length = random.randint(len_min, len_max)
    password = []

    for i in range(random_length):
        sign_number = random.randint(0,len(alfanumeric_signs['znaki_alfanumeryczne']))
        password.append(alfanumeric_signs['znaki_alfanumeryczne'][sign_number])

    return password

if __name__ == '__main__':

    #ex1
    print("EX1")
    print(create_list(100))
    print("\n")

    #ex2
    print("EX2")
    print(create_odd_numbers_list(50))
    print("\n")

    #ex3
    print("EX3")
    s: str = "24mdksmf435sdjfna0fjnsbfha0"
    print(get_numbers_from_string(s))
    print("\n")

    #ex4
    print("EX4")
    print_fibonacci_sequence(10)
    print("\n")

    #ex5
    print("EX5")
    print(create_alphabet_pairs())
    print("\n")

    #ex6
    print("EX6")
    print(create_password())
    print("\n")