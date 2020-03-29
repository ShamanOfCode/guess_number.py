
number = 23
cond = True

while cond:
    guessed = int(raw_input("Guess the number: "))
    cond = False

    if number == guessed:
        print("Congratulations, you guessed the number!!")
        
        cond = False # Das fuehrt zum Ende der while-Schleife
    elif (guessed < number):
        print("No, the number is a little higher.")
    else:
        print("No, the number is slightly lower.")
else:
    print("The while loop has ended.")
print("Finished")
