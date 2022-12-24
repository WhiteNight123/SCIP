def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a % 2 == 1 and b % 2 == 1 # You can replace this line!


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    "*** YOUR CODE HERE ***"
    sum = 1
    while n > 1:
        if n == 2:
            return sum * 2
        sum *= n * (n - 1);
        n -= 2
    return sum


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    "*** YOUR CODE HERE ***"
    if a < 0 and b < 0 and c < 0:
        return False
    if (a + b) > c and (a + c) > b and (b + c) and a:
        return True
    return False


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


def min_digit(x):
    """Return the min digit of x.

    >>> min_digit(10)
    0
    >>> min_digit(4224)
    2
    >>> min_digit(1234567890)
    0
    >>> # make sure that you are using return rather than print
    >>> a = min_digit(123)
    >>> a
    1
    """
    "*** YOUR CODE HERE ***"
    m = 9
    while x > -1:
        M = min(m, x % 10)
        x //= 10
    return m
