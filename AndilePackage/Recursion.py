"""
This is a function for a recursive sum of an array. 
"""
def _findSum(arr, N): 
     if len(arr)== 1: 
        return arr[0] 
     else: 
        return arr[0]+_findSum(arr[1:], N) 

def fibonacci(n):
    """
    This is a fibonacci function The function has been optimised with the use of memoization.

    Calculate nth term in fibonacci sequence
    
    Args:
        n (int): nth term in fibonacci sequence to calculate
    
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    
    Examples:
        >>> fibonacci(1)
        1        
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """
    #The cache is where reults will be stored in memory so that as the sequence gets longer and more complex it doesn't slow down
    fibonacci_cache = {}


    #this is to optimize the sequence to run faster as the sequence gets longer
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    #The fibonacci sequence and how it works through the numbers
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    '''Return nth term in fibonacci sequence
    from cache if the value is in a really high number'''
    fibonacci_cache[n] = value
    return value



def factorial(n):
    """
    check if number greater than 1 as there is no real test case for - or zero factorial
    we use while so that the code runs hopefully quicker but there is no real advantage in this
    unless you have something else running but this function we don't so it's just nice to have
    """
    while  n >= 1:
    #we return what the multiplication of the number that is our base case with all numbers smaller   
        return n * factorial(n - 1)
    
    #Return n! we will get 1 if we search for factorial of 1 hence this code
    return 1



def reverse(word):

    """
    Return a string that has been reversed
        Args:
            word (str): a string 
        Returns:
            str: word string reversed and given backwards
    
        Examples:
            >>> reverse('cheese')
            'eseehc'
            >>> reverse('banana')
            'ananab'
            >>> reverse('awesome')
            'emosewa'
    """
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]