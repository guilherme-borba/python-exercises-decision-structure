'''Make a program that asks which shift you study. Ask to enter M-Morning or V-Evening or N-Night. 
Print the message "Good Morning!", "Good Afternoon!" or good night!" or "Invalid Value!", as applicable.'''

shift = input(
    "Which shift you study [M-Mornig, V-Evening or N-Night]: ").upper()

if (shift == "M"):
    print("Good mornig!")
elif (shift == "V"):
    print("Good evening!")
elif (shift == "N"):
    print("Good night!")
else:
    print("Invalide value!")
