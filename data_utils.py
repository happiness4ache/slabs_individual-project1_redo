# Author: Nthabiseng

"""
This program calculates the averages and arranges the total amounts as South African Rand
"""

def calculate_average(num1,num2,num3,num4,num5):
    """
    this calculates and brings back the average of numbers
    :param: The five numbers are calculated
    :return: The mathematical average of the numbers
    """
    average = (num1 + num2 + num3 + num4 + num5)/5
    return average

def format_currency(amount):
    """
    This program structure the numbers as South African Rand
    :param amount: the total amount will be layed out
    :return: returning a string such as R150.50
    """
    currency_in_rand = "R" + str(round(amount,2))
    return currency_in_rand

