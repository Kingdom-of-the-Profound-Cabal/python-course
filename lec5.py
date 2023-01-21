#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
 The Fibonacci series is a mathematical sequence of numbers in which each number is the sum of the two preceding ones,
 usually starting with 0 and 1. The series goes as 0, 1, 1, 2, 3, 5, 8, 13, and so on.
 Each number in the series is referred to as a Fibonacci number. The Fibonacci series has many applications in mathematics,
 science, and engineering, including computer science, biology, and finance.
"""


def fibonacci_series(n: int) -> list:
    """
    This function takes an integer number n and returns a list of the Fibonacci series up to the nth number.
    
    Parameters:
    n (int): the number of terms of the series to be generated.
    
    Returns:
    list: a list of integers representing the fibonacci series up to the nth term
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    series = [0, 1]
    for i in range(2, n):
        series.append(series[i-1] + series[i-2])

    return series


# check if a script is being run directly or if it is being imported as a module into another script.
if __name__ == "__main__":
    print("I am the main script")
    # Test the function function
    print(fibonacci_series(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
