def is_prime(num):
    """
    check whether a number is prime or not.
    we iterate over all numbers between 2 and the sqrt of num
    (and not until num, to make it more efficient since no factor
    of num can be greater than the sqrt of num)
    :param num: number to check if its prime
    :type num: int
    """
    if num > 1:
       # check for factors
       for i in range(2, int(num** (1/2)) + 1):
           # if we found a factor return false
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               return False

    return True
