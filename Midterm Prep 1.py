# Define the function to extract 3-letter words starting with "b"
def print_three_letter_b_words(filename):
    """Reads a text file and prints three-letter words that start with 'b'."""
    try:
        with open(filename, "r") as file:
            words = file.read().split()  # Read and split words

        # Filter words that are exactly three letters and start with 'b'
        b_words = [word for word in words if len(word) == 3 and word.startswith("b")]

        # Print the matching words
        print("Three-letter words starting with 'b':", ", ".join(b_words))

    except FileNotFoundError:
        print("The file was not found.")


# Call the function with the actual filename
print_three_letter_b_words("input.txt")
