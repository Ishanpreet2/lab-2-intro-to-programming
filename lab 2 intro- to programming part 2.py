def get_positive_number(prompt):

    #A helper function to get a positive number from the user.
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def print_species_data(start_count, daily_increase, num_days):

    #A function to print the organisms/species data for each day.
 count = start_count 
 print(f"Day1: {count}")
 for day in range(2, num_days+1):
        count += count * (daily_increase / 100)
        print(f"Day {day:02d}: {count:.2f}")

# Get input from the user
start_count = get_positive_number("Enter the starting number of organisms/species: ")
daily_increase = get_positive_number("Enter the average daily percentage increase: ")
num_days = int(get_positive_number("Enter the number of days' worth of data to be printed: "))

# Print species data for each day
print_species_data(start_count, daily_increase, num_days)
