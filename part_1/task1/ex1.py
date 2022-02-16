##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## ex1
##

for i in range(1, 100) :
    if i%3 == 0 and i%5 != 0:
        print("Three")
    elif i%5 == 0 and i%3 != 0:
        print("Five")
    if i%3 == 0 and i%5 == 0:
        print("ThreeFive")
    else :
        print(i)
