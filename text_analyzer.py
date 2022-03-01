
"""author = Martin Rečka"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

SEPARATOR = 40 * "-"
title_words = 0
upper_words = 0
lower_words = 0
numbers_count = 0
numbers_sum = 0
lengths_of_words = dict()

name = input("Username: ")
password = input("Password: ")
print(SEPARATOR)

if name in USERS.keys() and USERS[name] == password:
    print(f"Welcome to the app, {name}.")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    exit()

print(SEPARATOR)
number = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print(SEPARATOR)

if not number.isnumeric():
    print("Wrong symbol, terminating the program...")
    exit()
else:
    number = int(number)
    if 0 < number <= len(TEXTS):
        pass
    else:
        print("Wrong number. terminating the program...")
        exit()

words_in_text = TEXTS[number-1].split()
all_words_count = len(words_in_text)

for word in words_in_text:
    word = word.strip(".,?!:")

    if len(word) not in lengths_of_words.keys():
        lengths_of_words[len(word)] = 1
    else:
        lengths_of_words[len(word)] += 1

    if word[0].isupper():
        title_words += 1
        if word.isupper():
            upper_words += 1
    elif word.islower():
        lower_words += 1
    elif word.isnumeric():
        numbers_count += 1
        word = int(word)
        numbers_sum += word

print(
    f"There are {all_words_count} words in the selected text.",
    f"There are {title_words} titlecase words.",
    f"There are {upper_words} uppercase words.",
    f"There are {lower_words} lowercase words.",
    f"There are {numbers_count} numeric strings.",
    f"The sum of all numbers is {numbers_sum}.",
    SEPARATOR,
    "LEN|   OCCURRENCES   |NR.",
    SEPARATOR,
    sep="\n"
)

for length, count in sorted(lengths_of_words.items()):
    print(f"""{str(length).rjust(3, " ")}|{str(count*"*").ljust(17, " ")}|{count}""")
print(SEPARATOR)
