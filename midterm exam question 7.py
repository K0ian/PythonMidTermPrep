def is_valid_url(url):
    """
    Checks if the given string is a valid URL.

    A valid URL must:
    - Start with "http://" or "https://"
    - Contain at least one "." after the protocol
    - Have at least one character before and after the "."

    :param url: The string to check
    :return: True if it's a valid URL, otherwise False
    """
    # Check if URL starts with "http://" or "https://"
    if url[:7] == "http://" or url[:8] == "https://":
        # Remove the protocol part
        no_protocol = url[7:] if url[:7] == "http://" else url[8:]

        # Check if there is at least one dot
        if "." in no_protocol:
            dot_index = no_protocol.find(".")  # Get position of first dot

            # Ensure there is at least one character before and after the dot
            if dot_index > 0 and dot_index < len(no_protocol) - 1:
                return True

    return False


# Test cases
test_urls = [
    "https://example.com",  # Valid
    "http://google.com",  # Valid
    "https://sub.domain.org",  # Valid
    "http://localhost",  # Invalid (No ".")
    "http://googlecom",  # Invalid (No ".")
    "google.com",  # Invalid (Missing "http://")
    "ftp://example.com",  # Invalid (Wrong protocol)
    "https://.com",  # Invalid (No domain before ".")
    "https://example.",  # Invalid (No domain after ".")
]

# Run the function and print results
validity_results = {url: is_valid_url(url) for url in test_urls}
print(validity_results)

