def calculator():
    num1 = float(input('Input your first number: '))
    operator = input('Input the operator (+, -, *, /): ')
    num2 = float(input('Input your second number: '))
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print('Cannot divide by zero!')
            return
    else:
        print('Invalid operator!')
        return
    print('Result: ', result)


calculator()