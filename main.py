import random

def generateString(lenght, upper_letter, numbers):
    string = ""

    for i  in range(0, lenght):
        num_rate = random.randint(0, 4)
        if (upper_letter) == True:
            if (numbers == True and num_rate == 1):
                string += str(random.randint(0, 9))
            else:
                string += chr(random.randint(ord('A'), ord('Z')))
        else:
            if (numbers == True and num_rate == 1):
                string += str(random.randint(0, 9))
            else:
                string += chr(random.randint(ord('a'), ord('z')))
    return string

error = False

try:
    input_lenght = int(input("Lenght: "))
except:
    error = True
    print("unvalid input")

if (error == False):
    input_upper_letter = input("Upper Letter (y/n): ")
    if (input_upper_letter == "y"):
        input_upper_letter = True
    else:
        input_upper_letter = False

if (error == False):
    input_numbers = input("Numbers (y/n): ")
    if (input_numbers == "y"):
        input_numbers = True
    else:
        input_numbers = False

if (error == False):
    print(generateString(input_lenght, input_upper_letter, input_numbers))
