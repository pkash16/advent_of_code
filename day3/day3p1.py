def search_largest(numbers, condition):
    largest = None
    largest_index = -1
    for index, number in enumerate(numbers):
        if condition(index, number):
            if largest is None or number > largest:
                largest = number
                largest_index = index
    return largest, largest_index   

input_lines = []
with open("input.txt", "r") as f:
    for line in f:
        input_lines.append(line.strip())

sum_final_numbers = 0
for line in input_lines:
    largest, largest_index = search_largest(line, lambda index, number: index != len(line)-1 )
    second_largest, second_largest_index = search_largest(line, lambda index, number: index > largest_index )
    final_number = int(f"{largest}{second_largest}")
    sum_final_numbers += final_number
    print(f"final number: {final_number}")
print(f"sum of final numbers: {sum_final_numbers}")