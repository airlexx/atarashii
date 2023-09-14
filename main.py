import random

def generateString(lenght, upper_letter):
    string = ""

    for i  in range(0, lenght):
        if (upper_letter) == True:
            string += chr(random.randint(ord('A'), ord('Z')))
        else:
            string += chr(random.randint(ord('a'), ord('z')))
    return string

input_lenght = int(input("Lenght: "))
input_upper_letter = input("Upper Letter (y/n): ")

if (input_upper_letter == "Y"):
    input_upper_letter = True
else:
    input_upper_letter = False

print(generateString(input_lenght, input_upper_letter))