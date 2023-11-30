sentence = input("Enter a sentence: ")

n1 = int(input("Enter the starting position (n1): "))
n2 = int(input("Enter the ending position (n2): "))

if n1 <= n2 and n1 >= 0 and n2 < len(sentence):
    modified_sentence = sentence[:n1] + sentence[n2 + 1:]

    print("Modified Sentence:", modified_sentence)
else:
    print("Invalid indices. Please ensure n1 <= n2 and within the string's range.")
