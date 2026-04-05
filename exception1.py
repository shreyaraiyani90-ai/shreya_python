try:
    number1 = int(input("enter a number"))
    number2 = int(input("enter anther number:"))
    result = number1 / number2
except ZeroDivisionError:
    print("you cannot divide by zero!")
except ValueError:
    print("please enter a valid number!")
else:
    print("Division successful! Result is:", result)
finally:
    print("This block alway run.")            

