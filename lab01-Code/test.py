def number_of_nine(n):
    """Return the number of 9 in each digit of a positive integer n.

    >>> number_of_nine(999)
    3
    >>> number_of_nine(9876543)
    1
    """
    "*** YOUR CODE HERE ***"
    res = 0
    while n > 8:
        if n % 10 == 9:
            res += 1
        n //= 10
    return res

number_of_nine(98790)