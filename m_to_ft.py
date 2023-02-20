height = float(input("Whats your height: "))

inches = int((height * 39.38) / 12)
inches_feet = (height * 39.38) % 12

print(f"You're: {inches}'{round(inches_feet)}")