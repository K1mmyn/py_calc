

def getInputAsFloat(msg):
    try:
        return float(input(msg))
    except:
        return

def multiple(a, b):
    return a * b

def divide(a, b):
    return a / b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def pow(a, b):
    return a ** b

while True:
    a = getInputAsFloat("Please enter a number:")
    b = getInputAsFloat("Please enter a number:")
    print("What operation? \n (*) Multipication \n (/) Division \n (+) Addition \n (-) Subraction \n (**) Power \n (==) Quit \n>", end="")
    method = input()
    match method:
        case "*":
            print(multiple(a, b))
        case "/":
            print(divide(a, b))
        case "+":
            print(add(a, b))
        case "-":
            print(sub(a, b))
        case "**":
            print(pow(a, b))
        case "==":
            break

        

