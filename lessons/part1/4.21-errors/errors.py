INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class InvalidPasswordError(Exception):
    pass

def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError("Password cannot be same as username!")
    elif password in INVALID_PASSWORDS:
        raise InvalidPasswordError("Invalid password!")
    return
       
    


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        validate_password(username, password)
    except InvalidPasswordError as err:
        print(err)
    else:
        account = create_account(username, password)

if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!
