SIMPLE CALCULATOR
-----------------

#Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!


.. code:: python

    a = input("Enter First Number: ")
    b = input("Enter Second Number: ")

    print("\nString Value(Commented)\n")

    # print(a , " + " , b , " = " , a+b)
    # print(a , " - " , b , " = " , a-b)
    # print(a , " x " , b , " = " , a*b)
    # print(a , " ÷ " , b , " = " , a/b)
    # print("Floored value of" , a , " ÷ " , b , " = " , a//b)
    # print("Remainder of" , a , " ÷ " , b ,  " = " , a%b)
    # print(a , " to the power " , b , " = " , a**b)

    print("Integer value")

    print(a , " + " , b , " = " , int(a)+int(b))
    print(a , " - " , b , " = " , int(a)-int(b))
    print(a , " x " , b , " = " , int(a)*int(b))
    print(a , " ÷ " , b , " = " , int(a)/int(b))
    print("Floored value of" , a , " ÷ " , b , " = " , int(a)//int(b))
    print("Remainder of" , a , " ÷ " , b ,  " = " , int(a)%int(b))
    print(a , " to the power " , b , " = " , int(a)**int(b))
    

.. code:: python

    def add(x, y):
      """Adds two numbers."""
      return x + y

    def subtract(x, y):
      """Subtracts two numbers."""
      return x - y

    def multiply(x, y):
      """Multiplies two numbers."""
      return x * y

    def divide(x, y):
      """Divides two numbers."""
      return x / y

    def main():
      """Prompts the user for two numbers and performs the desired operation."""
      operation = input("Please choose an operation: +, -, *, or / ")
      number_1 = float(input("Enter your first number: "))
      number_2 = float(input("Enter your second number: "))

      if operation == "+":
        print(number_1, "+", number_2, "=", add(number_1, number_2))
      elif operation == "-":
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
      elif operation == "*":
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
      elif operation == "/":
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
      else:
        print("Invalid operation.")

    if __name__ == "__main__":
      main()

