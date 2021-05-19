# Arian.programmer

print('Hi i\'m Calculator')

num1 = int(input('Enter your number1 : '))
num2 = int(input('Enter your number2 : ')) 

ask = input('''What addition and subtraction should I do between number1 and number2 ?
        +
        -
        *
        **
        /
        //
        %
        ''')  

if ask == '+':
    answer = num1 + num2
    print(answer)
elif ask == '-':
    answer = num1 - num2
    print(answer)
elif ask == '*':
    answer = num1 * num2
    print(answer)
elif ask == '**':
    answer = num1 ** num2
elif ask == '/':
    answer = num1 / num2
    print(answer)
elif ask == '//':
    answer = num1 // num2
    print(answer)
elif ask == '%':
    answer = num1 % num2
    print(answer)
