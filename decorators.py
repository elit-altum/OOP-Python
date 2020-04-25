# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrapper(user):
        if user['valid']:
            fn(user)
        else:
            print('Please authenticate first')
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
