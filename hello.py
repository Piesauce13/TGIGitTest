from time import sleep

from sqlalchemy import true

# print("Hello everyone!")

# num = 20
# studentName = "Alexander"

# x = y = z = 0
# a, b, c = 1,2,"hello"

# my_variable = 10
# my_variable = "Hello"
# my_variable = 3.14

# # const declaration
# PI = 3.14159
# MAX_SIZE = 100

# #delete variable from memory
# del my_variable

# # if condition
# if a > b: 
#     print("a is greater than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("a is less than b")

# Check if a number is positive, negative or zero
def check_number():
    print("\nCheck if a number is positive, negative or zero.")
    number = float(input("Enter a number: "))

    print("You entered:", number)
    if (number < 0):
        print("Negative number entered.")
    elif (number == 0):
        print("Zero entered.")
    else:
        print("Positive number entered.")

# Leap year
def leap_year():
    print("\nCheck if a year is a leap year.")
    year = int(input("Enter a year: "))  
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

# Calculator 
def calculator():
    print("\nSimple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        print(num1, "+", num2, "=", num1 + num2)
    elif operator == '-':
        print(num1, "-", num2, "=", num1 - num2)
    elif operator == '*':
        print(num1, "*", num2, "=", num1 * num2)
    elif operator == '/':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error: Division by zero.")
    else: 
        print("Invalid operator.")

# ticket pricing based on age
def ticket_pricing():
    print("\nTicket Pricing based on Age")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Your ticket costs $5.")
    elif age <= 65:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $7.")

# fruits = ["apple","banana", "cherry" ]

# for fruit in fruits:
#     print(fruit)

# count = 1

# while count <=5:
#     print("Count: ", count )
#     count += 1

# for i in range(10):
#     if i==3:
#         print("the loop will skip 3")
#         continue
#     elif i==7:
#         print("the loop will stop entirely at 7")
#         break
#     print("looping rn", i)


def countdown(count):
    print("Counting down from:", count)
    while count > 0:
        print("count:", count)
        count -= 1

def print_each_char(word):
    print("Printing each character in the word:", word)
    for index, char in enumerate(word, start=0):
        print(index, char)

def password_check():
    print("Password check with 3 attempts.")
    password = "password123"
    for i in range(3):
        user_input = input("Enter your password:")
        if user_input == password:
            print("Password Accepted! Welcome!")
            break
        else:
            print("Incorrect password. You have", 2 - i, "attempts left after waiting 1 minute.")
            if i < 2:
                sleep(60)   

def password_check2():
    print("try 3 times before wating 1 min to try again")
    password = "password123"
    attempts = 0
    while true:
        user_input = input("Enter your password:")
        attempts += 1
        if user_input == password:
            print("Password Accepted! Welcome!")
            break
        elif attempts < 3:
            print("try again.")
        else: 
            print("3 Attempts reached. You have to wait 1 minute.")
            sleep(60)
            attempts = 0
            
def us_to_eu_floor():
    us_floor = int(input("Enter US floor:"))
    if us_floor <= 0:
        return us_floor
    elif us_floor < 14:
        return us_floor-1
    else:
        return us_floor-2
    
def us_to_eu_floor_iternary(us_floor):
    return us_floor-1 if us_floor<14 else us_floor-2
    
def multiplication_table():
    num = int(input("Enter number for its multiplication table:"))
    for i in range(1, 11):
        print(num, "*", i, "=", num*i)

def helper(num, count):
    print(num, "*", count, "=", num*count)

def multiplication_table_recursive(num, count=10):
    if count == 0:
        return
    else:
        multiplication_table_recursive(num, count-1)
        helper(num, count)

def aboutlist():
    list = [1,2,3,4,5]

    list.append(6)
    print("add elelemnt at the end of the list:", list)
    list.insert(0,0)
    print("add element at a specific index:", list)
    list.extend([7,8,9])
    print("Add multiple elements to a list:", list)
    list.remove(5)
    print("remove the first occurence of a value:", list)
    list.pop()
    print("remove the element at the specific index and return it:", list)

aboutlist()

def aboutdict():
    student = {"name":"Panha", "age": 20}

    student["city"] = "Siem Reap"
    print(f"{student['name']} city is {student['city']}")

    student.keys()
    student.values()
    student.items()

aboutdict()

def main():
    # check_number()
    # leap_year()
    # calculator()
    # ticket_pricing()
    # countdown(10)
    # print_each_char("Hello")
    # password_check2()
    print("This US floor in Europe would be", us_to_eu_floor())
    multiplication_table()
    # multiplication_table_recursive(5)

# if __name__ == "__main__":
# main()