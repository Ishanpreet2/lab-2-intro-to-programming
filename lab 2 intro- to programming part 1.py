# Initial variables to hold total rainfall and count of months
total_rainfall = 0
num_months = 0

# Asking user for number of years
num_years = int(input("Enter the number of years: "))

# Loop through each year
for year in range(1, num_years+1):
    year_rainfall = 0
    
    # Loop through each month and ask user for rainfall
    for month in range(1, 13):
        rainfall_cm = float(input(f"Enter the rainfall in centimetres for Year {year}, Month {month}: "))
        year_rainfall += rainfall_cm
        total_rainfall += rainfall_cm
        num_months += 1
    
    # Calculate and display yearly and monthly average rainfall
    yearly_average = year_rainfall / 12
    print(f"Year {year} Total Rainfall: {year_rainfall} cm, Average Monthly Rainfall: {yearly_average:.2f} cm")

# Calculate and display overall average monthly rainfall
overall_average = total_rainfall / num_months
print(f"\nOverall Average Monthly Rainfall: {overall_average:.2f} cm")
