def count_bob_words(text):
    """
    Finds occurrences of words that start with 'b' and end with 'Bob'.

    :param text: The text to search through.
    :return: The number of matches found.
    """
    words = text.split()  # Split the text into words
    count = 0  # Initialize a counter

    for word in words:
        if word.startswith("b") and word.endswith("Bob"):  # Check conditions
            count += 1  # Increment count if match is found

    return count


# Test text including words that:
# - Start with "b" and end with "Bob" (valid matches)
# - Start with "b" but do not end with "Bob" (should not match)
# - End with "bob" (should not match because "b" must be uppercase)
test_text = """
bxyzBob bBob b123Bob b-testBob bbbbbBob bhelloBob
Bob Bob123 bxyzbob baBob bnumberbob BxyzBob
"""

# Call the function and print the result
print(count_bob_words(test_text))
