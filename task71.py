def calculate_increase_rate(start_amount, end_amount, weeks):
    increase_rate = ((end_amount - start_amount) / start_amount) / weeks
    return increase_rate


start_amount = 1000
end_amount = 1560
weeks = 6
increase_rate = calculate_increase_rate(start_amount, end_amount, weeks)
print("Процент увеличения суммы: {:.2%}".format(increase_rate))
