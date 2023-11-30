sequence = input("Enter a sequence: ")

# Initialize a count variable
count = 0

for i in range(1, len(sequence)):
    if sequence[i] == sequence[0]:
        count += 1
    else:
        break

print("Quantity of identical characters at the beginning:", count)
sequence = input("Enter a sequence: ")

# Determine the length of the sequence
length = len(sequence)

# В этом случае все символы могут быть одинаковыми, поэтому количество - это длина последовательности
count = length

print("Quantity of identical characters at the beginning:", count)
