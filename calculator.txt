def add(number1, number2):
  return number1 + number2

def subtract(number1, number2):
  return number1 - number2

def multiply(number1, number2):
  return number1 * number2

def divide(number1, number2):
  if number2 == 0:
    return "Error: Cannot divide by zero."
  return number1 / number2

def main():
  print("Welcome to the Simple Calculator!")

  while True:
    choice = input("Choose an operation (+, -, *, /): ")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    result = None

    if choice == "+":
      result = add(number1, number2)
    elif choice == "-":
      result = subtract(number1, number2)
    elif choice == "*":
      result = multiply(number1, number2)
    elif choice == "/":
      result = divide(number1, number2)
    else:
      print("Invalid operation, Please choose +, -, *, or /")

    if result is not None:
      print("Result: ", result)
      break

if __name__ == "__main__":
  main()