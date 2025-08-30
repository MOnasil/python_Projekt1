TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# user/password
usernames = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}

username = input("username: ")
password = input("password: ")
oddelovac = "-" *40
print(oddelovac)
if username in usernames and usernames[username] == password:
    print("Welcome to the app,", username)
    print(f"We have {len(TEXTS)} texts to be analyzed. ")

    cislo = input((f"Enter a number btw. 1 and {len(TEXTS)} to select:"))
    text = TEXTS[int(cislo) -1]
    split = text.split()
    

    print(f"There are {len(split)} words in the selected text")

    titlecase = sum(word.istitle() for word in split)
    print("There are", titlecase, "titlecase words")

    uppercase = sum(word.isupper() for word in split)
    print("There are", uppercase, "uppercase words")

    lowercase = sum(word.islower() for word in split)
    print("There are", lowercase, "lowercase words")

    pocet = sum(cislo.isdigit() for cislo in split)
    print("There are", pocet, "numeric strings")

    soucet = 0
    for cislo in split:
        if cislo.isdigit():
            soucet += int(cislo)

    print("Sum of all numbers:", soucet)
    print(oddelovac)
    print("LEN|   OCCURRENCES   |NR.")
    print(oddelovac)

    cetnost = {}
    for word in split:
        word_clean = ''
        for char in word:
            if char.isalnum():  
                word_clean += char
        if word_clean: 
            cetnost[len(word_clean)] = cetnost.get(len(word_clean), 0) + 1

    for delka in sorted(cetnost):
        hvezdy = "* " * cetnost[delka]
        print(f"{delka:>3} | {hvezdy:<25} | {cetnost[delka]:>2}")



else:
    print("unregistered user, terminating the program..")
