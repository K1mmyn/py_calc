print("Welcome to Kim's Custom Calculator")
end = ""
while end != "==":
    try:
        number_1 = input("First number: ")
        if number_1 == "==":
            break
        number_2 = input("Second number: ")
        if number_2 == "==":
            break
        print("What operation? \n (*) Multipication \n (/) Division \n (+) Addition \n (-) Subraction \n (**) Power \n (==) Quit \n>", end="")
        task = input()
        number_1 = float(number_1)
        number_2 = float(number_2)
        if task == "*":
            sum = number_1 * number_2
            print("Sum: " + str(sum))
        elif task == "/":
            sum = number_1 / number_2
            print('Sum: ' + str(sum))
        elif task == "+":
            sum = number_1 + number_2
            print('Sum: ' + str(sum))
        elif task == "-":
            sum = number_1 - number_2
            print('Sum:' + str(sum))
        elif task == "**":
            sum = number_1 ** number_2
            print("Sum: " + str(sum))
        elif task == "==":
            print("Thank for using Kim's Calculator! ")
            break
        else:
            print("Sorry, I don't know that! ")
    except:
        print("Please enter a valid number")
        continue



