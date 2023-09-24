# Write a program that checks whether a typed letter is a vowel or a consonant.

letter = input("Type a letter: ").upper()

if letter in ["A", "E", "I", "O", "U"]:
    print("Letter is a vowel.")
else:
    print("Letter is a consonant.")
