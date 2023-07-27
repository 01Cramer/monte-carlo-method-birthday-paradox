import random
import numpy as np
import matplotlib.pyplot as plt

### Main params of simulation
tests_on_groups_of_x_people = 100000
number_of_people_in_group = []
for i in range(2, 52, 2):
    number_of_people_in_group.append(i)


number_of_people_in_group_and_probability_of_pair = {}

months = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

for i in range(len(number_of_people_in_group)):
    x = number_of_people_in_group[i]
    matchings = 0  # Matching - at least two people sharing a birthday
    for j in range(tests_on_groups_of_x_people):
        genereted_birthdays = []

        for birthday in range(x):
            birthday = random.choice(months)
            if (
                birthday == "Jan"
                or birthday == "Mar"
                or birthday == "May"
                or birthday == "Jul"
                or birthday == "Aug"
                or birthday == "Oct"
                or birthday == "Dec"
            ):
                birthday = birthday + " " + str(random.randint(1, 31))
            elif birthday == "Feb":
                birthday = birthday + " " + str(random.randint(1, 28))
            else:
                birthday = birthday + " " + str(random.randint(1, 30))

            genereted_birthdays.append(birthday)

        for birthday in genereted_birthdays:
            if genereted_birthdays.count(birthday) > 1:
                matchings += 1
                break

    probability_of_sharing_birthday = matchings / tests_on_groups_of_x_people
    probability_of_sharing_birthday = round(probability_of_sharing_birthday, 2)

    number_of_people_in_group_and_probability_of_pair[
        x
    ] = probability_of_sharing_birthday

# Graph
x = list(number_of_people_in_group_and_probability_of_pair.keys())
y = list(number_of_people_in_group_and_probability_of_pair.values())

plt.plot(x, y, linestyle="dotted", linewidth=2, color="black")
plt.grid(True)
plt.xlabel("Number of people")
plt.ylabel("Probability of a pair")
plt.xticks(range(min(x), max(x) + 1, 2))
plt.yticks([i / 10 for i in range(int(min(y) * 10), int(max(y) * 10) + 2, 1)])

# Interpolation
y_val = 0.5
x_interp = np.interp(y_val, y, x)
print(x_interp)
plt.plot(
    [x_interp, x_interp], [0, y_val], color="red", linestyle="dashed", linewidth=0.9
)
plt.plot([2, x_interp], [y_val, y_val], color="red", linestyle="dashed", linewidth=0.9)
plt.show()
