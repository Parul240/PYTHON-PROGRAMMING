                                                   SIMPLE CALCULATOR

#Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!


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
    
