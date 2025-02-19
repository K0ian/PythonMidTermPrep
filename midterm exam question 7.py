import random

# Step 1: Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Step 2: Modify the list based on given conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    elif random_numbers[i] < 50:
        # Replace numbers lower than 50 with "XX", but keep 50 unchanged
        random_numbers[i] = "XX"

# Step 3: Print the final list
print(random_numbers)
