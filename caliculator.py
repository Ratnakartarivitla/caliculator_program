#task - 11
operand1 = int(input("Enter the 1st operand : "))
operand2 = int(input("Enter the 2nd operand : "))
operator = input("Enther the operation + or - or * or / or % : ")

if operator == "+":
  print(operand1+operand2)
elif operator == "-":
  print(operand1-operand2)
elif operator == "*":
  print(operand1*operand2)
elif operator == "/":
  print(operand1/operand2)
elif operator == "%":
  print(operand1%operand2)
else:
  print("invalid operator - operation cannot be performed")
