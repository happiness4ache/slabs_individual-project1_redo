# Author: Nthabiseng

import data_utils
import random
import datetime

def main():
    """
    This program produces 5 random transaction amounts,prints today's date and the amounts and their averages formatted as Rands
    :param: none
    :return: none
    """

    random_num1 = random.randint(50, 500)
    random_num2 = random.randint(50, 500)
    random_num3 = random.randint(50, 500)
    random_num4 = random.randint(50, 500)
    random_num5 = random.randint(50, 500)

    amount_1 = int(input("Enter a number: "))

    todays_date = datetime.date.today()

    average_value = data_utils.calculate_average(random_num1, random_num2, random_num3, random_num4, random_num5)

    amount1_rands = data_utils.format_currency(amount_1)

    print("today's_date is :", todays_date)
    print("The 5 random numbers: ", random_num1, random_num2, random_num3, random_num4, random_num5)
    print("The average of the 5 random numbers:", average_value)
    print("The currency amount in rands:", amount_1)

if __name__ == "__main__":
    main()

