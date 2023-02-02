def calculate(number_1, number_2):
    task = input('Выберите операцию:+, -, *, /')
    if task == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif task == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif task == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif task == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('Такой операции нет:')


number_1 = int(input('Введите  число: '))
number_2 = int(input('Введите  число: '))
calculate(number_1, number_2)