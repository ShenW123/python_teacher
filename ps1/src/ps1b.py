# -*- coding: utf-8 -*-


def calculate_raise(portion_saved, current_salary, salary_raise):
    new_salary = current_salary * (1 + salary_raise)
    new_monthly_salary = new_salary / 12
    new_saved_monthly = portion_saved * new_monthly_salary
    return new_saved_monthly, new_salary

def main(annual_salary, portion_saved, semi_annual_raise, total_cost):
    portion_down_payment = total_cost*0.25
    current_savings = 0
    r = 0.04
    saved_monthly, current_salary = calculate_raise(portion_saved, annual_salary, 0)
    current_months = 0
    while portion_down_payment > current_savings:
        current_months = current_months + 1
        current_savings = current_savings + current_savings * r / 12
        current_savings = current_savings + saved_monthly
        if (current_months % 6 == 0):
            saved_monthly, current_salary = calculate_raise(portion_saved, current_salary, semi_annual_raise)
    return current_months


if __name__ == "__main__":

    x = input('Enter your annual salary: ')
    y = input('Enter the percent of your salary to save, as a decimal: ')
    a = input('Enter the semi­annual raise, as a decimal: ')
    z = input('Enter the cost of your dream home: ')
    result = main(x, y, a, z)
    print('The result is: ' + str(result))