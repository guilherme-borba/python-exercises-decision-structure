# Write a Program that checks whether a typed letter is "F" or "M".
# According to the letter: F - Female, M - Male, Invalid Sex.

sex = input("What your sex [F-Famale or M-Male]: ").lower()

if (sex == "f"):
    print("You is female.")
elif (sex == "m"):
    print("You is male.")
else:
    print("Invalid sex")
