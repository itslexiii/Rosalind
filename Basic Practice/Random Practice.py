# Try while True and use function in a loop.


def joinname(fn, ln):
    print('Hello! '+fn+' '+ln+'.')


while True:
    print('Please tell me your name.')
    print('Enter Q to quit.')
    fn = input('First name: ')
    if fn == 'Q':
        print('End.')
        break
    ln = input('Last name: ')
    if fn == 'Q':
        print('End.')
        break
    joinname(fn, ln)
