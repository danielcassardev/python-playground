#Exercise 1 from https://www.practicepython.org/

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
#tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date
# the next year).

#Extra 1: Add on to the previous program by asking the user for another number and printing out that many copies of
#the previous message.
#Extra 2: Print out that many copies of the previous message on separate lines.

name=input("Welcome to the age game, what is your name? ")
# capture input of name as a string
age=int(input("and what is your age? "))
# capture input of age as an integer
message_qty=int(input("and give me one more number "))
# capture additional value for Extra 1
current_year = 2025
# hard code the current year
age_100 = (current_year +(100-age))
# calculate the year the player will turn 100
while message_qty > 0:
    print(f"{name} you will turn 100 years old in year {age_100}")
    # print the result back to the player
    message_qty=message_qty-1
    # reduce message_qty count by 1


