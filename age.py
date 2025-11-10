try:
    age = int(input("Enter Your Age: "))
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
except ValueError:
    print("Please enter a valid integer for age")
