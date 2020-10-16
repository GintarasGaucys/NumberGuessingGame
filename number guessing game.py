import random


def hintdivide(hintlist, n, num):
    for i in range(n):
        randiv = random.randrange(2, 20)
        if num % randiv == 0:
            hintlist.append("The number divisible by " + str(randiv))


def hintmultiple(hintlist, n, num):
    for i in range(n):
        randmult = random.randrange(3, 15)
        hintlist.append("The number multiplied by x is " + str(randmult * num))


def hintbiggerorsmaller(hintlist, n, num):
    for i in range(n):
        rand1 = random.randrange(1, 30)
        if rand1 > num:
            hintlist.append("The number is smaller then " + str(rand1))
        elif rand1 < num:
            hintlist.append("The number is bigger then " + str(rand1))
        rand2 = random.randrange(30, 60)
        if rand2 > num:
            hintlist.append("The number is smaller then " + str(rand2))
        elif rand2 < num:
            hintlist.append("The number is bigger then " + str(rand2))
        rand3 = random.randrange(60, 100)
        if rand3 > num:
            hintlist.append("The number is smaller then " + str(rand3))
        elif rand3 < num:
            hintlist.append("The number is bigger then " + str(rand3))


def hints(num):
    hints = []
    hintdivide(hints, 10, num)
    hintmultiple(hints, 5, num)
    hintbiggerorsmaller(hints, 4, num)
    return hints


guesses = 10
guessed = False

thenumber = random.randrange(1, 101)
hintslist = hints(thenumber)
previoushints = []

while not guessed and guesses != 0:
    print("Guess a number\nYou have", guesses, "guesses left.")
    print("Previous hints: ", previoushints)
    idx = random.randrange(0, len(hintslist))
    print("Hint:\n" + hintslist[idx])
    previoushints.append(hintslist[idx])
    hintslist.pop(idx)
    guess = int(input())

    if guess == thenumber:
        guessed = True
    else:
        guesses = guesses - 1
        print("Wrong!\n")

print("\nCongratulations! You guessed the number")

