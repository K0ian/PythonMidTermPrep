def find_words(filename):
    """
    prints the 3 letter words starting with b
    :param filename: the name of the file
    :return: Nothing
    """
    with open(filename, 'r') as f:
        for line in f:
            # need to break down the line into words
            words = line.split() # by default splits by space
            # check words
            for word in words:
                if len(word) == 3 and word.upper()[0] == "B" :
                    print(word)
find_words("input.txt")



punctuation = ",.?!'"

def find_words(filename):
    """
    prints the 3 letter words starting with b
    :param filename: the name of the file
    :return: Nothing
    """
    with open(filename, 'r') as f:
        for line in f:
            # sanitize line
            for p in punctuation:
                line = line.replace(p, "")
            # need to break down the line into words
            words = line.split() # by default splits by space
            for word in words:
                if len(word) == 3 and word.upper[0] in "Bb":
                    print(word)
    find_words("input.txt")


def get_multiple_6():
    """
    Returns a multiple of 6 that was entered by the user.
    :return: into a number
    """
    while True:
        try:
            n = input("Please give me a multiple of 6: ")
            n = int(n) # convert to int
            # how to check if it is a multiple of 6?
            if n / 6 == n // 6:
                return n
            else:
                print("that is not a multiple of 6")
        except ValueError:
            print("you have not entered a number")
print(get_multiple_6())
