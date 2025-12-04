def search_largest(numbers, condition):
    largest = None
    largest_index = -1
    for index, number in enumerate(numbers):
        if condition(index, number):
            if largest is None or number > largest:
                largest = number
                largest_index = index
    return largest, largest_index

def search_largest_n_digit(numbers, n):

    found_numbers = []

    #look for the first digit.
    largest, largest_index = search_largest(numbers, lambda index, number: index < len(numbers) - (n-1))

    found_numbers.append(largest)

    # look for the next n-1 digits.
    for i in range(1, n):
        next_largest, largest_index = search_largest(numbers, lambda index, number: index > largest_index and index < len(numbers) - (n - (i + 1)))
        found_numbers.append(next_largest)
    
    return int(''.join(found_numbers))

input_lines = []
with open("input.txt", "r") as f:
    for line in f:
        input_lines.append(line.strip())

sum_final_numbers = 0
for line in input_lines:
    final_number = search_largest_n_digit(line, 12)
    sum_final_numbers += final_number
    print(f"final number: {final_number}")
print(f"sum of final numbers: {sum_final_numbers}")