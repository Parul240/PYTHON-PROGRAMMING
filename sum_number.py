#1
'''
Add two numbers
'''

x = 5
y = 10
print(x + y)




#2
'''
Python3 program to add two numbers with user input
'''
 
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum)) 




#3
'''
Python program to add two numbers using def sum
'''

def sum(x, y):
    sum = x + y
    return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))



