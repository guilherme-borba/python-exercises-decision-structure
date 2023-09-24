'''Make a program to read two partial notes from a student. The program must calculate the 
average achieved per student and present:
A) The message "Approved", if the average achieved is greater than or equal to seven;
B) The message "Failed", if the average is less than seven;
C) The message "Approved with Distinction", if the average is equal to ten.'''

note1 = float(input("Enter a note: "))
note2 = float(input("Enter a outher note: "))

average = (note1 + note2) / 2

if (average >= 7 and average < 10):
    print("Approved.")
elif (average < 7):
    print("Failed.")
elif (average == 10):
    print("Approved with distinction.")
