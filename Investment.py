# Leslie A. Borst
# 9/23/17
# Interest on Principle
# Determine the total interest and final value of the investment

# Declare variables

principle = int()
time_yrs = int()
int_rate = float()
total_int = float()
final_val = float()

# Get inputs from the user

principle = int(input('Enter the Principle Value of your investment: \t\t\t$'))
time_yrs = int(input('Enter the Time(in years) you plan to save your investment:\t'))
int_rate = float(input('Enter the Rate (2% = 0.02) you will collect on your investment:\t'))

# Calculate the user inputs to generate outputs

total_int = principle * int_rate * time_yrs
final_val = principle + total_int

# Display results

print('The final value of your investment will be: \t\t\t$', format(final_val, '.2f'))

