# -*- coding: utf-8 -*-


def main(annual_salary, portion_saved, total_cost):
    portion_down_payment = total_cost*0.25
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary/12
    saved_monthly = monthly_salary * portion_saved
    current_months = 0
    while portion_down_payment > current_savings:
        current_months = current_months + 1
        current_savings = current_savings + current_savings * r / 12
        current_savings = current_savings + saved_monthly
    return current_months


if __name__ == "__main__":

    x = input('Enter your annual salary: ')
    y = input('Enter the percent of your salary to save, as a decimal: ')
    z = input('Enter the cost of your dream home: ')
    result = main(x, y, z)
    print('The result is: ' + str(result))