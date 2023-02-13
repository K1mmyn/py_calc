from simple_colors import *
import math
import modules


modules.invalid_message

def quit_message():
    print(cyan("\nThanks for using Kim's Calculator \n", 'bold'))
    quit()


def getInputAsFloat(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print(cyan("\nPlease enter a number... ", 'bold'))
            continue

def getInputAsFloatValid(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print(cyan("\nPlease Enter a valid command ", 'bold'))
            continue

def squareroot(a):
    return math.sqrt(a)

print("\nWelcome To The Master Calculator \n")
print("Type 'Help' if this is your first time!")
starting_help = input("Otherwise, Press the Enter key: ").lower()
if starting_help == "help":
    print("\nIf you are looking to do Simple Interest or Conversion, Please enter the command 'Co' ") #Add Trig
    print("If you are looking to use a Calculator, Please enter the command 'Ca' \nIf you are looking to square root numbers, Please enter your number twice when asked \n \
Enter '00' at anytime to quit")

while True:
    print("")
    print(green('Main Menu', 'bold')) 
    q = input("\n(Ca)lculator \n(Co)nvertor \n(Q)uit \n\n > ").lower()
    if q == "q":
        quit_message()
    if q == "co":
        while True:
            print("\n (90) Main Menu \n (1) Convert Kgs to Lbs \n (2) Convert Lbs to Kgs \n (3) Simple Interest \n (4) NZD to USD \n (5) USD to NZD \n (6) KRW to NZD \n \
(7) Inches to CMs \n (8) CMs to Inches \n (9) Kms to Miles \n (10) Miles to Kms \n (00) Quit \n")
            convertor_method = getInputAsFloatValid("> ")
            if convertor_method == 00:
                quit_message()
            if convertor_method == 90:
                break
            match convertor_method:
                case 1:
                    weight_kgs = getInputAsFloat("\nWeight in Kgs: ")
                    if weight_kgs == 00:
                        quit_message()
                    conversion_kg_to_lbs = weight_kgs / 0.45
                    print(yellow(f"\nYour Weight in Lbs is {conversion_kg_to_lbs}Lbs", 'bold'))
                    break
                case 2:
                    weight_lbs = getInputAsFloat("\nWeight in Lbs: ")
                    if weight_lbs == 00:
                        quit_message()
                    conversion_lbs_to_kgs = weight_lbs * 0.45
                    print(yellow(f"\nYour Weight in Kgs is {conversion_lbs_to_kgs}Kgs", 'bold'))
                    break
                case 3:
                    p = getInputAsFloat("\nPrinciple: ")
                    if p == 00:
                        quit_message()
                    t = getInputAsFloat("Time: ")
                    if t == 00:
                        quit_message()
                    r = getInputAsFloat("Rate: ")
                    if r == 00:
                        quit_message()
                    t2 = (p * t * r / 100)
                    summary = (yellow(f"\nFrom your original amount of {p}$ over the period of {t} years borrowing at a rate {r}% your simple interest is {t2}$ "))
                    print(summary)
                    break
                case 4:
                    nzd_amount = getInputAsFloat("\nAmount in NZD: ")
                    if nzd_amount == 00:
                        quit_message()
                    conversion_nzd_to_usd = nzd_amount * 0.6337
                    print(yellow(f"\nUSD Amount: ${conversion_nzd_to_usd}"))
                    break
                case 5:
                    us_amount = getInputAsFloat("\nAmount in USD: ")
                    if us_amount == 00:
                        quit_message()
                    conversion_usd_to_nzd = us_amount * 1.5775
                    print(yellow(f"\nNZD Amount: ${conversion_usd_to_nzd}"))
                    break
                case 6:
                    krw_amount = getInputAsFloat("\nAmount in Korean Won: ")
                    if krw_amount == 00:
                        quit_message()
                    converstion_krw_to_nzd = krw_amount * 0.00079
                    print(yellow(f"\nNZD Amount: {converstion_krw_to_nzd}"))
                    break
                case 7:
                    inches_amount = getInputAsFloat("\nAmount in Inches: ")
                    if inches_amount == 00:
                        quit_message()
                    coversion_inches_to_cm = inches_amount * 2.54
                    print(yellow(f"\nCM Amount: {coversion_inches_to_cm}cm "))
                    break
                case 8:
                    cm_amount = getInputAsFloat("\nAmount in CM: ")
                    if cm_amount == 00:
                        quit_message()
                    conversion_cm_to_inches = cm_amount * 0.393701
                    print(yellow(f"\nInches Amount: {conversion_cm_to_inches}inches "))
                    break
                case 9:
                    kms_amount = getInputAsFloat("\nAmount in KMs: ")
                    if kms_amount == 00:
                        quit_message()
                    conversion_kms_to_miles = kms_amount * 0.6213
                    print(yellow(f"\nMiles: {conversion_kms_to_miles}"))
                    break
                case 10:
                    miles_amount = getInputAsFloat("\nAmount in Miles: ")
                    if miles_amount == 00:
                        quit_message()
                    converstion_miles_to_kms = miles_amount * 1.60934
                    print(yellow(f"\nKMs Amount: {converstion_miles_to_kms}"))
                    break
                case _:
                    print("Sorry, I don't understand that! \nPlease Enter a valid command.. ")
                    continue
    elif q == "ca":
        while True:
            print("\n (90) Main Menu \n (1) Addition \n (2) Subraction \n (3) Multiplication \n (4) Division \n (5) Power \n (6) Squarroot \n "
                "(00) Quit \n")
            print("What operation would you like to do? ")
            method = getInputAsFloatValid("\n> ")
            if method == 00:
                quit_message()
            if method == 90:
                break
            if method == 1 or 2 or 3 or 4 or 5 or 6:
                a = getInputAsFloat("\nEnter your first number.. ")
                if a == 00:
                    quit_message()
                b = getInputAsFloat("Enter your second number.. ")
                if b == 00:
                    quit_message()
            else:
                print("Please enter valid command")
            match method:
                case 1:
                    answer_add = lambda a, b: a + b
                    print(yellow("\nYour Answer is: " + str(answer_add(a, b)), 'bold'))
                    break
                case 2:
                    answer_sub = lambda a, b: a - b
                    print(yellow("\nYour Answer is: " + str(answer_sub(a, b)), 'bold'))
                    break
                case 3:
                    answer_time = lambda a, b: a * b
                    print(yellow("\nYour Answer is: " + str(answer_time(a,b)), 'bold'))
                    break
                case 4:
                    answer_division = lambda a, b: a / b
                    print(yellow("\nYour Answer is: " + str(answer_division(a, b)), 'bold'))
                    break
                case 5:
                    answer_power = lambda a, b: a ** b
                    print(yellow("\nYour Answer is: " + str(answer_power(a, b)), 'bold'))
                    break 
                case 6:
                    print(yellow("\nYour Answer is: " + str(squareroot(a)), 'bold'))
                    break
                case _:
                    print("Sorry, I don't understand that! \nPlease Enter a valid command.. ")
                    continue
                #what ever user input is a str check if the str matches the commands
                # what we need to do is get the input the user sends us, do a count to see if what the user sent us is in the list 
                # if the count returns 0 there is nothing on the list making it invalid if there is a count >= 1 its valid and will continue to our match case             
    else:
        
        modules.invalid_message()