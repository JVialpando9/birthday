from datetime import date
import time

print("welcomeeee")
name = input("What is your name? ")
month = input("Enter your birth month: >") 
day= input("Enter your birth day: >")
year = input("Enter your birth year: >")

print("your birthday is:", month, day, year)
for i in range(2): 
    print("Happy birthday to you")
    time.sleep(1)

print("Happy birthday dear.", name)

td = date.today()  
print(td)