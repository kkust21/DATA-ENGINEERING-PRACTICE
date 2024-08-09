'''try:
    num1 = int(input("enter the number1: "))
    num2 = int(input("enter the number2: "))
    result = num1 / num2
    print(num1, "/", num2, "=", result)
    x = [7, 8, 9]#3
    x[len(x)] = 23#len[2]=23
except ZeroDivisionError:
    print("Error:Denominator cannot be zero")
except IndexError:
    print("index you are using is not present in the list")
'''
try:
    num = int(input("enter the number1: "))
    assert num % 2 == 0
except AssertionError:
    print("you have entered odd number")
else:
    num = 0
    print("the program is end")

yob = int(input("enter year of birth: "))
age = 2024-yob
if age<18:
    raise Exception(f'Enter age for PG program {age}')
def divide(x,y):
    try:
        if y==0:
            raise ZeroDivisionError("Cannot divide by zero")
        result=x/y
        return result
    except(ZeroDivisionError,AssertionError) as e:
        print("error",e)

