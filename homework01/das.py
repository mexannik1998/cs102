def is_prime(n):
    """
    Tests to see if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    z = 0
    for i in n:
        if n % i == 0 :
            z +=1
    if z == 2 :
        tf = 1
    else:
        tf = 0
    return tf