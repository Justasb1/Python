def convert_centimeters_to_dmc(cm):
    # Calculate meters
    meters = cm // 100
    # Calculate decimeters
    remaining_cm = cm % 100
    decimeters = remaining_cm // 10
    # Calculate remaining centimeters
    centimeters = remaining_cm % 10
    
    return meters, decimeters, centimeters

# Input in centimeters
centimeters = int(input("Enter the length in centimeters: "))

# Convert and get the result
meters, decimeters, remaining_centimeters = convert_centimeters_to_dmc(centimeters)

# Display the result
print(f"{centimeters} centimeters is equal to {meters} meters, {decimeters} decimeters, and {remaining_centimeters} centimeters.")
