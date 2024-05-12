"""
 projekt_1.py: první projekt do Engeto Online Python Akademie
 author: Marek Hes
 email: marekhes99@centrum.cz
 discord: marek_09805
 """

from texts import TEXTS
from copy import deepcopy
registered_users = {"bob": "123",
                    "ann": "pass123",
                    "mike": "password123",
                    "liz": "pass123"}
# přihlášení
user = input("username:")
password = input("password:")

if user in registered_users and registered_users[user] == password:
    print("-" * 40)
    print("Welcome to the app, " + user + "\nWe have 3 texts to be analyzed.")
    print("-" * 40)
# výběr textu
    number_input = int(input("Enter a number btw. 1 and 3 to select: "))
    print("-" * 40)

#statistiky
    if 0 < number_input <= int(len(TEXTS)):
        text = TEXTS[int(number_input) - 1]

        # operace pro získání správných hodnot do statistik
        words = text.split()
        title = []
        upper = []
        lower = []
        number = []
        word_count = len(words)
        for word in words:
            if word.istitle():
                title.append(word)
            if word.isupper() and word.isalpha():
                upper.append(word)
            if word.islower():
                lower.append(word)
            if word.isdigit():
                number.append(int(word))
        sum_for_numbers = sum(number)

        # výpis statistik
        print("There are", word_count, "words in the selected text.")
        print("There are", len(title), "titlecase words.")
        print("There are", len(upper), "uppercase words.")
        print("There are", len(lower), "lowercase words.")
        print("There are", len(number), "numeric strings.")
        print("The sum of all the numbers", sum_for_numbers)
# graf
        # nadpisy sloupců grafu
        print("-" * 40)
        print("LEN|  OCCURENCES  |NR.")
        print("-" * 40)

        # očištění textu o interpunkci a speciální znaky pro vytvoření grafu
        punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        cleaned_text = deepcopy(text)
        for word in cleaned_text:
            if word in punc:
                cleaned_text = cleaned_text.replace(word, "")
        cleaned_words = cleaned_text.split()

        # operace pro získání správných hodnot do grafu
        frequencies = {}
        for word in cleaned_words:
            frequencies[len(word)] = frequencies.get(len(word),0) + 1
        # výpis hodnot grafu
        for key, value in sorted(frequencies.items()):
            print(f"{key:3}|{value * '*':<14}|{value}")
    # upozornění - neexistující číslo textu
    else:
        print("The number You've selected is not valid, terminating the program..")
# upozornění - neregistrovaný uživatel
else:
    print("$ python projekt1.py\nusername:" + user + "\npassword:" + password +
"\nunregistered user, terminating the program..")
