try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Result: ", result)

try:
    print(x)
except:
    print("An exception occurred")

    try:
        print(x)
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")


def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount


try:
    new_balance = withdraw(200, 100)
except ValueError as e:
    print(f"Error: {e}")
