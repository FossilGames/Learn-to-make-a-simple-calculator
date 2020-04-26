#Calculator
#Assign some values to the calculator
#It must be a float
print("""Only 2 numbers can be added,subtracted, multiplicated or divided
Type + for addition,- for subtraction, * for multiplication, / for division
""")
a = float(input("Enter the first number: "))
op = input("Enter arithmetical operator")
b = float(input("Enter the second number: "))
if op == "+" :
 print(a+b)
elif op == "-" :
 print(a-b)
elif op == "*" :
 print(a*b)
elif op == "/" :
 print(a/b)
else :
 print("Invalid Arithmetic operator")


