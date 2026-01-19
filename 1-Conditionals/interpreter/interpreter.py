equation = input("Input (x y z): ")
x, y, z = equation.split(" ")
x = float(x)
z = float(z)
if y == "+":
    result = x+z
elif y == "-":
    result = x-z
elif y == "/":
    result = x/z
elif y == "*":
    result = x*z
print(result)