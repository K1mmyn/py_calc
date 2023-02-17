from simple_colors import *
import math
import modules

# round all numbers

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
    print(green('\nMain Menu', 'bold')) 
    q = input("\n(1) Calculator \n(2) Unit Conversion \n(3) Money Conversion & Fraction, Percentage & Decimals \n(4) Pythagoras & Trig \n(00) Quit \n\n > ")
    if q == '00':
        quit_message()
    if q == '1':
        while True:
            print("\n(90) Main Menu \n(1) Addition \n(2) Subraction \n(3) Multiplication \n(4) Division \n(5) Power \n(6) Squarroot \n(00) Quit \n")
            print("What operation would you like to do? ")
            method = getInputAsFloatValid("\n> ")
            if method == 00:
                quit_message()
            if method == 90:
                break
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
                    print(yellow("\nYour Answer is: " + str(round(answer_add(a, b),2)), 'bold'))
                    break
                case 2:
                    answer_sub = lambda a, b: a - b
                    print(yellow("\nYour Answer is: " + str(round(answer_sub(a, b),2)), 'bold'))
                    break
                case 3:
                    answer_time = lambda a, b: a * b
                    print(yellow("\nYour Answer is: " + str(round(answer_time(a,b),2)), 'bold'))
                    break
                case 4:
                    answer_division = lambda a, b: a / b
                    print(yellow("\nYour Answer is: " + str(round(answer_division(a, b), 2)), 'bold'))
                    break
                case 5:
                    answer_power = lambda a, b: a ** b
                    print(yellow("\nYour Answer is: " + str(round(answer_power(a, b),2)), 'bold'))
                    break 
                case 6:
                    print(yellow("\nYour Answer is: " + str(round(squareroot(a),2)), 'bold'))
                    break
                case _:
                    modules.invalid_message()             
    elif q == '2':
        while True:
            print("\n(90) Main Menu \n(1) Convert Kgs to Lbs \n(2) Convert Lbs to Kgs \n(3) Simple Interest \n(4) Inches to CMs \n(5) CMs to Inches \
\n(6) Kms to Miles \n(7) Miles to Kms \n(00) Quit \n")
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
                    print(yellow(f"\nYour Weight in Lbs is {round(conversion_kg_to_lbs, 2)}Lbs", 'bold'))
                    break
                case 2:
                    weight_lbs = getInputAsFloat("\nWeight in Lbs: ")
                    if weight_lbs == 00:
                        quit_message()
                    conversion_lbs_to_kgs = weight_lbs * 0.45
                    print(yellow(f"\nYour Weight in Kgs is {round(conversion_lbs_to_kgs, 2)}Kgs", 'bold'))
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
                    summary = (yellow(f"\nFrom your original amount of {p}$ over the period of {t} years borrowing at a rate {r}% your simple interest is {round(t2,2)}$ "))
                    print(summary)
                    break
                case 4:
                    inches_amount = getInputAsFloat("\nAmount in Inches: ")
                    if inches_amount == 00:
                        quit_message()
                    coversion_inches_to_cm = inches_amount * 2.54
                    print(yellow(f"\nCM Amount: {round(coversion_inches_to_cm, 2)}cm "))
                    break
                case 5:
                    cm_amount = getInputAsFloat("\nAmount in CM: ")
                    if cm_amount == 00:
                        quit_message()
                    conversion_cm_to_inches = cm_amount * 0.393701
                    print(yellow(f"\nInches Amount: {round(conversion_cm_to_inches, 2)}inches "))
                    break
                case 6:
                    kms_amount = getInputAsFloat("\nAmount in KMs: ")
                    if kms_amount == 00:
                        quit_message()
                    conversion_kms_to_miles = kms_amount * 0.6213
                    print(yellow(f"\nMiles: {round(conversion_kms_to_miles, 2)}"))
                    break
                case 7:
                    miles_amount = getInputAsFloat("\nAmount in Miles: ")
                    if miles_amount == 00:
                        quit_message()
                    converstion_miles_to_kms = miles_amount * 1.60934
                    print(yellow(f"\nKMs Amount: {round(converstion_miles_to_kms, 2)}"))
                    break
                case _:
                    modules.invalid_message()
                    
                #what ever user input is a str check if the str matches the commands
                # what we need to do is get the input the user sends us, do a count to see if what the user sent us is in the list 
                # if the count returns 0 there is nothing on the list making it invalid if there is a count >= 1 its valid and will  to our match case 
    elif q == "3":
        while True:
            print("\n(90) Main Menu \n(1) NZD to USD \n(2) USD to NZD \n(3) KRW to NZD \n(4) Fraction to Decimal \n(5) Fraction to Percentage \
\n(6) Percentage to Decimal \n(7) Percentage to Fraction \n(8) Decimal to Percentage \n(9) Decimal to Fraction \n(00) Quit") 
            method = getInputAsFloatValid('\n> ')
            if method == 00:
                quit_message()
            if method == 90:
                break
            match method:
                case 1:
                    nzd_amount = getInputAsFloat("\nAmount in NZD: "); conversion_nzd_to_usd = nzd_amount * 0.6337
                    print(yellow(f"\nUSD Amount: ${round(conversion_nzd_to_usd, 2)}"))
                    break
                case 2:
                    us_amount = getInputAsFloat("\nAmount in USD: "); conversion_usd_to_nzd = us_amount * 1.5775
                    print(yellow(f"\nNZD Amount: ${round(conversion_usd_to_nzd, 2)}"))
                    break
                case 3:
                    krw_amount = getInputAsFloat("\nAmount in Korean Won: "); converstion_krw_to_nzd = krw_amount * 0.00079
                    print(yellow(f"\nNZD Amount: {round(converstion_krw_to_nzd, 2)}"))
                    break
                case 4:
                    a = getInputAsFloat("\nNumerator: "); b = getInputAsFloat("Denominator: "); answer_fraction_to_decimal = lambda a,b : a * (100 / b)
                    print(yellow(f'\nYour Answer is: {round(answer_fraction_to_decimal(a, b) / 100 , 2)}'))
                case 5:
                    a = getInputAsFloat("\nNumerator: "); b = getInputAsFloat("Denominator: "); answer_fraction_to_percentage = lambda a,b: a * (100 / b)
                    print(yellow(f'\nYour Answer is: {round(answer_fraction_to_percentage(a,b), 2)}%'))
                case 6:
                    a = getInputAsFloat("\nPercentage: "); answer_percentage_to_decimal = lambda a : a / 100
                    print(yellow(f'\nYour Answer is: {round(answer_percentage_to_decimal(a), 2)}'))
                case 7:
                    a = getInputAsFloat("\nPercentage: ")
                    print(yellow(f"\nYour Answer is: {a}/100")) #make code understand how to simplify
                case 8:
                    a = getInputAsFloat("\nDecimal: "); answer_decimal_to_percentage = lambda a : a * 100
                    print(yellow(f'\nYour Answer is: {answer_decimal_to_percentage(a)}%'))
                case 9:
                    a = getInputAsFloat("\nDecimal: "); answer_decimal_to_fraction = lambda a : a * 100
                    print(yellow(f'\nYour Answer is {round(answer_decimal_to_fraction(a))}/100'))
                case _:
                    modules.invalid_message()            
    elif q == '4':
        while True:
            print("\n(90) Main Menu \n(1) Pythagorean theorem \n(2) Find Opposite with Hypoteonuse \n(3) Find Hypoteonuse with Adjacent \n(4) Find Adjacent with Opposite \
\n(5) Find Theta with Opposite & Hypoteonuse \n(6) Find Theta with Adjacent & Hypoteonuse \n(7) Find Theta with Opposite & Adjacent \n(00) Quit")
            method = getInputAsFloatValid('\n> ')
            if method == 00:
                quit_message()
            if method == 90:
                break
            match method:
                case 1: 
                    x = getInputAsFloat("\nOpposite Length: "); y = getInputAsFloat("Adjacent Length: ")
                    hypoteonuse_answer = lambda x,y : (x**2) + (y**2)
                    print(yellow(f'\nYour Hypoteonuse Length is: {round(math.sqrt(hypoteonuse_answer(x,y)),2)}', 'bold'))
                case 2:
                    x = getInputAsFloat("\nTheta: "); y = getInputAsFloat("Hypoteonuse Length: ")
                    print(yellow(f'\nYour Opposite Length is: {round((math.sin(math.radians(int(x)))) * y, 2)}'))
                case 3:
                    x = getInputAsFloat("\nTheta: "); y = getInputAsFloat("Adjacent Length: ")
                    print(yellow(f'\nYour Hypoteonuse Length is: {round((y / (math.cos(math.radians(int(x))))), 2)}'))
                case 4:
                    x = getInputAsFloat("\nTheta: "); y = getInputAsFloat("Opposite Length: ")
                    print(yellow(f'\nYour Adjacent Length is: {round((y / (math.tan(math.radians(int(x))))), 2)}'))
                case 5:
                    x = getInputAsFloat("\nOpposite Length: "); y = getInputAsFloat("Hypoteonuse Length: ")
                    print(yellow(f'\nYour Theta is: {round(math.degrees(math.asin(x/y)),2)}'))
                case 6:
                    x = getInputAsFloat("\nAdjacent Length: "); y = getInputAsFloat('Hypoteonuse Length: ')
                    print(yellow(f'\nYour Theta is: {round(math.degrees(math.acos(x/y)),2)}'))
                case 7:
                    x = getInputAsFloat('\nOpposite Length: '); y = getInputAsFloat('Adjacent Length; ')
                    print(yellow(f'\nYour Theta is: {round(math.degrees(math.atan(x/y)),2)}'))
                case _:
                    modules.invalid_message()  
    else:       
        modules.invalid_message()

# n = 1
# num = input("Numbers you want to add")
# for i in range(n):
#    a,b = map(int, num.split())
#    print(a + b)