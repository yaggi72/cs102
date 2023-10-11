def Calculator(num1,num2,action):
    '''

    :param num1: Число формата целое или с плавающей точкой
    :param num2: Число формата целое или с плавающей точкой
    :param action: Возможные действия: "+", "-", "*", "/"
    :return: Ошибку во вводе или результат действия
    '''
    actions = '+-*/'
    figures = '0123456789.'
    flaq = True
    for figure in str(num1):
        if figure not in figures:
            flaq = False
            return 'Ошибка ввода'

    for figure in str(num2):
        if figure not in figures:
            flaq = False
            return 'Ошибка ввода'

    if str(action) not in actions:
        flaq = False
        return 'Ошибка ввода'

    if (flaq == True) and action == '+':
        return num1 + num2

    if (flaq == True) and action == '-':
        return num1 - num2

    if (flaq == True) and action == '*':
        return num1 * num2

    if (flaq == True) and action == '/':
        return num1 / num2

print(Calculator(2,"fvb",'*'))