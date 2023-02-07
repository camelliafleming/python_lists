"""
Author:  Camellia Fleming
Course:  CSC 121
Assignment:  Lab Lesson 09 - Part 2
Description:  Generate 20 random numbers between 1 and 100, inclusive, and store them in a list
"""
import random


randlist = []
for i in range(20):
    randlist.insert(0,random.randint(1,100))

print(randlist)
