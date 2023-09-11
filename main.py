import random

def generateString(lenght, upper_letter):
    string = ""

    for i  in range(0, lenght):
        if (upper_letter) == True:
            string += chr(random.randint(ord('A'), ord('Z')))
        else:
            string += chr(random.randint(ord('a'), ord('z')))
    return string