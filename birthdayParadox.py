import random
from matplotlib import pyplot as plt

def addCompleteBirthdayToList(numOfBirthdays, monthsTuple, completeBirthdaysList):
    for birthdayToGenerate in range(0, numOfBirthdays):
        birthdayToGenerate = random.choice(monthsTuple)
        if birthdayToGenerate == 'Jan' or birthdayToGenerate == 'Mar' or birthdayToGenerate == 'May' or birthdayToGenerate == 'Jul' or birthdayToGenerate == 'Aug' or birthdayToGenerate == 'Oct' or birthdayToGenerate == 'Dec':
            birthdayToGenerate = birthdayToGenerate + " " + str(random.randint(1, 31))
        elif birthdayToGenerate == 'Feb':
            birthdayToGenerate = birthdayToGenerate + " " + str(random.randint(1, 28))
        else:
            birthdayToGenerate = birthdayToGenerate + " " + str(random.randint(1, 30))
        completeBirthdaysList.append(birthdayToGenerate)


print("Welcome to birthday paradox simulator!")
print("This application is an simple example of Monte Carlo method.")
print("You will be able to see the probability of two people having birthday on the same day in a given group of people!")
print("Let\'s have fun! Press enter: ")
input()

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
completeBirthdays = []
listOfInputs = []
listOfOutputs = []

print("How many groups you want to check ?: ")
numberOfGroups = int(input())

groupNumber = 1
inProgram = True
while inProgram:
    print(f"Type quantity of group {groupNumber}: ")
    numberOfBirthdays = int(input())
    listOfInputs.append(numberOfBirthdays)
    print(f"Generating {numberOfBirthdays} birthdays 10,000 times...")
    print("Press Enter to begin...")
    input()
    print("Running 10,000 simulations...")

    matching = 0
    counter = 10000

    while counter > 0:
        matching_found = False
        del completeBirthdays[:]    # Deletes all the elements in the array
        addCompleteBirthdayToList(numberOfBirthdays, months, completeBirthdays)
        for i in range(numberOfBirthdays):
            for j in range(i + 1, numberOfBirthdays):
                if completeBirthdays[i] == completeBirthdays[j]:
                    matching_found = True
                    matching = matching + 1
                    break
            if matching_found:
                break
        counter = counter - 1

    percentage_of_matching = (matching / 10000) * 100
    print(
        f"Out of 10,000 simulations of {numberOfBirthdays} people, there was a matching birthday in that group {matching} times.")
    print(
        f"This means that {numberOfBirthdays} people have a {round(percentage_of_matching, 2)} % chance of having a matching birthday in their group. ")
    listOfOutputs.append(percentage_of_matching)
    numberOfGroups -= 1
    groupNumber += 1
    if numberOfGroups == 0:
        inProgram = False

#   Additional values to make graph more accuracy
listOfInputs.append(0)
listOfOutputs.append(0)

listOfInputs.append(5)
listOfOutputs.append(2.7)

listOfInputs.append(60)
listOfOutputs.append(99.4)

listOfInputs.append(100)
listOfOutputs.append(99.99)

listOfInputs.sort()
listOfOutputs.sort()

print()
print("Now you can see summary of your\'s simulations: ")
print("Press enter: ")
input()

plt.plot(listOfInputs, listOfOutputs)
plt.title("Birthday Problem")
plt.xlabel("Number of people")
plt.ylabel("Probability of pair")
plt.show()

print("If you want to compare your results with the authentic graph go to: https://en.wikipedia.org/wiki/Birthday_problem")