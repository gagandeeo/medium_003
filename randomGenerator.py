import random

def generateRandomNumber():
    randomNumber = random.randint(9000000, 23000000)
    return randomNumber

if __name__ == "__main__":
    numberOfRandomNumbers = int(input("How many numbers should the random file hold?:"))

    fileToBeWrittenTo = open("randomNumbers.txt","w")

    for randomNumberCount in range(900, numberOfRandomNumbers + 1):
        randomNumber = generateRandomNumber()
        if (randomNumberCount == numberOfRandomNumbers):
            fileToBeWrittenTo.write(str(randomNumber))
            break
        fileToBeWrittenTo.write(str(randomNumber)+",")
