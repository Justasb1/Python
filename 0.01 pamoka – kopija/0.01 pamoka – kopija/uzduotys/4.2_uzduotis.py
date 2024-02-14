# Input the 5-digit number as a string
number_str = input("Enter a 5-digit number: ")

# Ensure the input is a valid 5-digit number
if len(number_str) != 5 or not number_str.isdigit():
    print("Please enter a valid 5-digit number.")
else:
    # Convert each digit to an integer
    first_digit = int(number_str[0])
    second_digit = int(number_str[1])
    fifth_digit = int(number_str[4])

    # Calculate the sum
    digit_sum = first_digit + second_digit + fifth_digit

    print(f"The sum of the first, second, and fifth digits is: {digit_sum}")
