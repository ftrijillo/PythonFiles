daily_balances = [107.92, 108.67, 109.86, 110.15]

def show_balances(daily_balances):
    num_balances = len(daily_balances)

    for day in range(num_balances - 3, num_balances - 1):
        balance_slice = daily_balances[day : day + 2]

        days_ago = num_balances - day
        # use positive number for printing
        print("slice starting %d days ago: %s" % (abs(days_ago), balance_slice))

show_balances(daily_balances)