num1=int(input("Enter num1:\n"))
num2=int(input("Enter num2:\n"))
print("Enter the operation you want to perform\n")
option=int(input("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n"))
match option:
   case 1:
      print(f"The sum of {num1} and {num2} is {num1 + num2}")
   case 2:
      print(f"The difference of {num1} and {num2} is {num1 - num2}")
   case 3:
      print(f"The product of {num1} and {num2} is {num1 * num2}")
   case 4:
      if num2==0:
         print("Division by zero is not allowed")
      else:
         print(f"The quotient of {num1} and {num2} is {num1 / num2}")
   case _:
        print("Invalid option")