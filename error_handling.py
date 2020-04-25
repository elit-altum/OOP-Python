# error handling with python

while True:
    try:
        number = int(input('Enter a number: '))
        print(number)
        print(10 / number)
    except ValueError as err:  # catches value errors
        print(f'Please enter valid input: {err}')
    except ZeroDivisionError:  # catches tryna divide by 0
        print('Cannot divide by zero!')
    else:
        print('Thank You!')
        break
    finally:
        print('I am finally!')
