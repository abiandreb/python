def check_item(i):
    """
    Function check if i is aliquot 3, 5 or 15
    :param i: value to check
    :type i: int

    :return: FizzBus if 'i' is multiple of 15, Buzz if 'i' is multiple of '5', return Buzz if 'i' is multiple of '3' and
    return 'i' if non of conditions is applied
    """
    if not i % 15:
        return 'FizzBuzz'

    elif not i % 3:
        return 'Fizz'

    elif not i % 5:
        return 'Buzz'

    else:
        return i


for item in range(1, 101):
    print(check_item(item))
