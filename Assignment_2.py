import random

x = random.randint(1,10)



def generateInt():
    x = random.randint(1, 10)
    return x

def guessInt():
    z = 0
    while z != x:

        y = input("Guess a number between 1 and 10: ")
        z = int(y)
        if z == x:
            break
        print(' Wrong try again!')
        print()
    print()
    print('Correct!')

def main():
    generateInt()
    guessInt()


if __name__ == '__main__': main()
