# Simple Calculator Program

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Modulus (%)")
print("7. Power (**)")

choice = input("Enter your choice (1-7): ")

print("\nResult:")

if choice == '1':
    print(num1 + num2)

elif choice == '2':
    print(num1 - num2)

elif choice == '3':
    print(num1 * num2)

elif choice == '4':
    print(num1 / num2)

elif choice == '5':
    print(num1 // num2)

elif choice == '6':
    print(num1 % num2)

elif choice == '7':
    print(num1 ** num2)

else:
    print("Invalid choice!")
