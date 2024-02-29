def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

if __name__ == '__main__':

    continue_calculating = True

    n1 = float(input('What is the first number?: '))
    n2 = float(input('What is the second number?: '))
    while continue_calculating:
        for v in operations:
            print(v)
        operation_symbol = input('Pick an operation: ')
        calc_function = operations[operation_symbol]
        answer = calc_function(n1,n2)
        print(f'{n1} {operation_symbol} {n2} = {answer}')
        option = input(f'Type y to continue calculating with {answer}, or type n to start a new calculation: ')
        if option in 'yYsS':
            n1 = answer
            print(f'First number is: {answer}')
            n2 = float(input('What is the second number?: '))
        if option in 'nN':
            continue_calculating = False