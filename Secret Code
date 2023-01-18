# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode



import random
print("Hello Boys and Girls!! What's Up??")
inp = int(input('''Press 1 if you want to type the message in coded form
Press 2 if you want to decode the Message\n'''))
if inp == 1:
    s = input("Type your Message that you want to code\n")
    letters = s.split(" ")
    ran = "qwertyuiopasdfghjklzxcvbnm"
    print("The Coded Message is ")
    for letter in letters:
        if(len(letter)<3):
            for i in range(len(letter)):
                print(letter[len(letter)-i-1],end="")
            print(end=" ")
        elif(len(letter)>=3):
            letter = letter+letter[0]
            letter = letter.removeprefix(letter[0])
            # print(letter)
            for i in range(3):
                letter += random.choice(ran[random.randint(0,25)])
                letter = random.choice(ran[random.randint(0,25)]) + letter

            print(letter,end=" ")
elif inp == 2:
    s = input("Type your Coded Message that you want to decode\n")
    letters = s.split(" ")
    for letter in letters:
        if(len(letter)<3):
            for i in range(len(letter)):
                print(letter[len(letter)-i-1],end="")
            print(end=" ")
        elif(len(letter)>=3):
            letter = letter.removeprefix(letter[:3])
            letter = letter.removesuffix(letter[-3:])
            letter = letter[len(letter)-1] + letter
            letter = letter.removesuffix(letter[len(letter)-1])
            print(letter,end=" ")
        else:
            print("Invalid Input")
