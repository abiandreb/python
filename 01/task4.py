def deposit_calc(years, percent, amount, reinvestment=0):
    """
    Function calculate income of deposit investment
    :param years: years of deposit. Type int
    :param percent: percents of deposit. Type int
    :param amount:  investment amount. Type int
    :param reinvestment amount. 1 by default
    :return: amount of income
    :rtype: int
    """
    if not reinvestment:

        income = amount * (1 + years * percent / 100)

    else:

        income = amount * (1 + percent / 100) ** reinvestment

    return round(income, 2)


print(deposit_calc(5, 12, 1000))
