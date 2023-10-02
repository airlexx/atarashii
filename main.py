import random

def welcome():
    print("Welcome to atarashii!")
    print("by airlex\n")
    print("Simple password generator\n")

def generateString(lenght, upper_letter, numbers, special_char):
    string = ""
    special_char_array = ['!','#','?','%', '*', '$', '+', '-', '@', '&', '_']

    for i  in range(0, lenght):
        num_rate = random.randint(0, 4)
        special_rate = random.randint(0, 6)
        if (upper_letter):
            if (numbers == True and num_rate == 1):
                string += str(random.randint(0, 9))
            if (special_char and special_rate == 1):
                string += str(random.choice(special_char_array))
            else:
                string += chr(random.randint(ord('A'), ord('Z')))
        else:
            if (numbers == True and num_rate == 1):
                string += str(random.randint(0, 9))
            if (special_char and special_rate == 1):
                string += str(random.choice(special_char_array))
            else:
                string += chr(random.randint(ord('a'), ord('z')))
    return [True, string]

def userInput(mode: int, default: bool|int):
    result = default
    if (mode == 0):
        try:
            n = int(input("Enter password size: "))
            if (n <= 0):
                print("Unvalid password size")
                return [False, ""]
            return [True, n]
        except:
            print("Unvalid input")
            return [False, ""]

    if (mode == 1):
        entry = input("Do you want capital letters? (y/N): ").lower().strip()

    if (mode == 2):
        entry = input("Do you want numbers? (Y/n): ").lower().strip()

    if (mode == 3):
        entry = input("Do you want special characters? (y/N): ").lower().strip()

    match entry:
        case "y":
            result = True
        case "n":
            result = False
        case "":
            result = default
        case _:
            print("Unvalid input")
            return [False, ""]
    
    return [True, result]

welcome()

r0 = userInput(0, 4)

if (r0[0]):
    r1 = userInput(1, False)

if (r0[0] and r1[0]):
    r2 = userInput(2, True)

if (r0[0] and r1[0] and r2[0]):
    r3 = userInput(3, False)

if (r0[0] and r1[0] and r2[0] and r3[0]):
    print("\nPassword: " + generateString(r0[1], r1[1], r2[1], r3[1])[1])
