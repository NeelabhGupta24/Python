#global variables
global result
result = 0
#functions
def add(num1,num2):
    global result
    result = num1+num2
    print(result)
def subtract(num1,num2):
    global result
    result = num1-num2
    print(result)
def multiplay(num1,num2):
    global result
    result = num1*num2
    print(result)
def divide(num1,num2):
    global result
    result = num1/num2
    print(result)
first_number = float(input(">"))
while True:
    print(first_number)
    operator = input("Operator (+,-,*,/,quit) >")
    if operator == 'quit':
        break
    else:
        second_number = float(input(">"))
        if operator=='+':
            add(num1=first_number,num2=second_number)
        elif operator == '-':
            subtract(num1=first_number,num2=second_number)
        elif operator == '*':
            multiplay(num1=first_number,num2=second_number)
        elif operator == '/':
            divide(num1=first_number,num2=second_number)
        else:
            print("Enter a valid operator (+,-,*,/,quit)")

    first_number = result