# Monte-Carlo-method-birthday-paradox

## According to wikipedia.org: "In probability theory, the birthday problem asks for the probability that, in a set of n randomly chosen people, at least two will share a birthday. The birthday paradox refers to the counterintuitive fact that only 23 people are needed for that probability to exceed 50%." In my project I used Monte Carlo method to solve this problem.

## Overview
I followed particular pattern of Monte Carlo method:
1. Defining a domain of possible inputs - In this problem, the domain consists of all possible dates represented in the form {day month}, where the range of days depends on the month. 
2. Generating inputs randomly - I conducted 100k simulations of groups with n randomly chosen people. I used values of n ranging from 2 to 50, with a step size of 2.
3. Performing deterministic computation on the inputs - I checked for matching (i.e., at least two people sharing a birthday) in a single simulation.
4. Aggregating the results - I calculated the percentage of matchings and drew conclusions based on the data.

## Results
According to the generated graph, it can be seen that only 23 people are needed for that probability to exceed 50%, which is equal to computations and confirms the correctness of this method.
![Wykres](https://github.com/01Cramer/Monte-Carlo-Method-Birthday-Paradox/assets/115926987/4e10010f-8221-463d-8c6d-527650aa1758)











