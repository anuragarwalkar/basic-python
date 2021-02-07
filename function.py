# Position arguents
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')
    return f'welcome on board {first_name}'

greet_user('anurag', 'arwalkar')


# Keyword arguments
greet_user(last_name = 'anurag', first_name = 'arwalkar')