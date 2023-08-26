#Alinura Sultanova
#07/17/2023
#This program asks for the starting day number and the length of your stay, then tells you the
# number of day of the week you will return on

# Prompt the user to enter the starting day number and length of stay
start_day = int(input("Enter the starting day number (0 for Sunday, 1 for Monday, ..., 6 for Saturday): "))
stay_length = int(input("Enter the length of your stay (number of nights): "))

# Calculate the day of the week you will return on
return_day = (start_day + stay_length) % 7

# Print the day of the week you will return on
print("You will return on day number", return_day)

#Finish