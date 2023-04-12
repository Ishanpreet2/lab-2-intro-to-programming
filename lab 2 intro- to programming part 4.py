# Define a function to initialize the list with the name "myNumbers"
def initialize_list():
    return [1,2,3,4,5,6,7,8,9,10]

# Call the initialize_list() function to create the list
myNumbers = initialize_list()

# Print the list to the console using a for loop
print("All numbers in the list:")
for numers in myNumbers:
    print(numers)

# Define a function to find and print all the elements from the list that are greater than 5
def find_greater_than_five(numbers_list):
    print("Numbers greater than 5:")
    for numbers in numbers_list:
        if numbers > 5:
            print(numbers)

# Call the find_greater_than_five() function with the myNumbers list as an argument
find_greater_than_five(myNumbers)

