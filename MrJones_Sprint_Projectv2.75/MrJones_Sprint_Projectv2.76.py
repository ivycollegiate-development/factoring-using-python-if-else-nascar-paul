# List all of the factors of a value
def list_factors(n):
    # Explain the line of code below
    return [i for i in range (1, n+1) if n % i == 0] # This will take whatever number we put in and check for factors using a list
if __name__ == '__main__': # Checks to see if the application is running locally
    user_input = input('Please enter a number here: ') # Ask the user for a number
try:
    # Convert that user input to an interger
    number = int(user_input)
    # Check to see if the number is positive or negative
    if number <= 0:
        print('Please enter a positive number.')
    else:
        # Get the factors for that value input
        factors = list_factors(number)
        # Print the factors of the input value
        print(f'The factors of {number} are {factors}')
except ValueError:
    #Handles the exception negative values or 0
    print('That is an invalid number. Please input a positive interger.')