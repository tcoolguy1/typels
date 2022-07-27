month = ("January","February","March","April","May","June","July","August","September","October","November","December",)
profits = ("20000","25000","30000","60000","40000","50000","55000","70000","45000","35000","65000","50000",)
max_profit = max(profits)
max_index = profits.index(max_profit)
print(max_index)
max_month = month[max_index]
print("The Maximum Profit of " + str(max_profit) + " was recorded in the month of " + str(max_month))

min_profit = min(profits)
min_index = profits.index(min_profit)
print(min_index)
min_month = month[min_index]
print("The Minimum Profit of " + str(min_profit) + " was recorded in the month of " + str(min_month))
