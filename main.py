print("Basic Calculator")
print(
  "~ This is a console based calculator, where one can operate on two integers,\n operate on two floats & even operate on two complex numbers & their combinations."
)
input("Press Enter to Continue...")

while True:
  calculator_type = input(
    "\nWhich calculator do you want to use?\n"
    "1. Operate on two Integers\n"
    "2. Operate on two Floats\n"
    "3. Operate on two Complex Numbers\n"
    "4. Operate on an Integer & a Float or Vice-Versa\n"
    "5. Operate on a Float & a Complex or Vice-Versa\n"
    "6. Operate on an Integer & a Complex or Vice-Versa\n"
    "\nEnter the number of your choice: ")

  if calculator_type in ["1", "2", "3", "4", "5", "6"]:
    x = input("Enter first number: ")
    a = input("Operator: ")
    y = input("Enter second number: ")
  else:
    print("Invalid choice. Exiting.")
    exit()

  if '.' in x or '.' in y:
    x = float(x)
    y = float(y)
  elif 'j' in x or 'j' in y:
    x = complex(x)
    y = complex(y)
  else:
    x = int(x)
    y = int(y)

  if a == "+":
    ans = x + y
  elif a == "-":
    ans = x - y
  elif a == "*":
    ans = x * y
  elif a == "/":
    if y != 0:
      ans = x / y
    else:
      print("Cannot divide by Zero")
      exit()
  elif a == "//":
    ans = x // y
  else:
    print("Invalid Operator")
    exit()

  print("Answer is:", ans)
  continue_executing = input(
    "Do you want to perform another calculation? (yes/no): ")
  if continue_executing.lower() != "yes":
    print("Thankyou for using the service.")
    break
