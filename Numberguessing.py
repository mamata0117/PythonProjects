import random
secretnumber=random.randint(1,100)
while True:
    usernumber=int(input("Enter a number between 1 and 100: "))
    if usernumber<secretnumber:
        print("Too low! Try again.")
    elif usernumber>secretnumber:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break
    