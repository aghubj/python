#functions

def addnum(num1, num2):
    print("addition of", num1, 'and', num2, ':', num1 + num2)

def multnum():
    print("multiplication of", num1, 'and', num2, ':', num1 * num2)

def divnum():
    print("division of", num1, 'and', num2, ':', num1 / num2)


retry = 'y'
print("this is small calculator:")

while retry == 'y' or retry == 'Y':
    num1 = float(input('please enter num1:'))
    num2 = float(input('please enter num2:'))
    opr = input('please enter + or 1 for addition, * or 2 for multiplication, / or 3 for division: ')

    if opr == '+' or opr == '1':
        addnum(num1, num2)
    elif opr == '*' or opr == '2':
        multnum()
    elif opr == '/' or opr == '3':
        divnum()
    else:
        print('wrong choice!!!')

    retry = input('do you want to run it again(y/n): ')

