import random

random_numbers = [random.randrange(0, 49, 1) for random_number in range(20)]
print(random_numbers)

squared_numbers = [random_num**2 for random_num in random_numbers]
print(squared_numbers)
