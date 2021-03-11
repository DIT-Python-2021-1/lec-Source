def add(a, b):
    return a + b


def substract(a, b):
    return a - b


# a, b = 10, 20

while True:
    a = input("a : ")
    if a != 'q':
        # a = input("a : ")
        b = input("b : ")
        print(a, '+', b, '=', add(int(a), int(b)))
        print("-------------------")
    else:
        print('good bye')
        exit(0)