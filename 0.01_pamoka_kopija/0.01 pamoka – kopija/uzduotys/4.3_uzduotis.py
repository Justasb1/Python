# Find the 5-digit number
for number in range(10000, 100000):
    # Convert the number to a string to access individual digits
    number_str = str(number)

    if len(number_str) == 5:
        # Extract the digits
        first_digit = int(number_str[0])
        second_digit = int(number_str[1])
        third_digit = int(number_str[2])
        fourth_digit = int(number_str[3])
        fifth_digit = int(number_str[4])

        # Check if the condition is met
        if first_digit + second_digit + fifth_digit == third_digit * fourth_digit:
            print("The 5-digit number that meets the condition is:", number)
            break
