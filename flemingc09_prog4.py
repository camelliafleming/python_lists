"""
Author:  Camellia Fleming
Course:  CSC 121
Assignment:  Lab Lesson 09 - Part 4
Description:  Generate 2 lists of 10 random numbers and
perform list operations: combine, sort, slice
"""
import random


r_list1 = []
r_list2 = []

#Generate 2 lists with random integers between 1 and 100, inclusive
for a in range(10):
    r_list1.insert(0,random.randint(1,100))

for b in range(10):
    r_list2.insert(0,random.randint(1,100))

print('List 1: ', r_list1)
print('List 2: ', r_list2)

#Combine the 2 lists
combined = r_list1 + r_list2
print('Combined List: ', combined)


#Sort the lists
combined.sort()
print('Sorted List: ', combined)


#List Slicing - 5 Biggest Items
print('5 Largest Numbers: ', combined[-6:-1])

