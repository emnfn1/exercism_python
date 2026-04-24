def is_armstrong_number(number):
    number = str(number)
    power = len(number)
    t = 0
    for digit in number:
        t += int(digit) ** power

    if t == int(number):
        return True
    return False
