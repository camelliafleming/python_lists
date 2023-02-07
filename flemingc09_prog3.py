"""
Author:  Camellia Fleming
Course:  CSC 121
Assignment:  Lab Lesson 09 - Part 3
Description:  Using random list from part 2, create 2 empty lists and append even and odd numbers to their respective lists
"""
import random

#create lists
randlist = []
odd_list = []
even_list = []

#iterate through random numbers and insert into randlist
for i in range(20):
    randlist.insert(0,random.randint(1,100))

#iterate through elements of randlist to check if even or odd
for elements in randlist:
    if elements % 2 == 0:
        even_list.append(elements)
    else:
        odd_list.append(elements)

print('Evens: ', even_list)
print('Odds: ', odd_list)





