def days_since_birthday(birthday):
    """
    Calculates how many whole years have passed since the given birthday
    and returns the total number of days (ignoring the birth year and current year).

    :param birthday: A string in the format "DD-MM-YYYY"
    :return: The total number of days (whole years * 365)
    """
    # Extract the birth year from the input string
    birth_year = int(birthday[-4:])  # The last 4 characters represent the year

    # Set the current year manually
    current_year = 2024

    # Calculate the number of whole years between birth and current year
    whole_years = current_year - birth_year - 1  # Excluding birth year and current year

    # Multiply by 365 to get the number of days
    total_days = whole_years * 365

    return total_days

# Your birthday in the given format "DD-MM-YYYY"
your_birthday = "07-01-2004"

# Calculate the days passed
days_passed = days_since_birthday(your_birthday)

# Print the result
print(f"Days passed since your birthday (excluding birth year and current year): {days_passed}")
