
word = input("Введите слово: ")

characters = []
found_chars = set()

for char in word:
    if char in found_chars:
        characters.append(char)
    else:
        found_chars.add(char)

if len(characters) == 2:
    print("Две одинаковые буквы в слове:", characters)
else:
    print("В этом слове нет двух абсолютно одинаковых букв.")
