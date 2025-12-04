# advent of code 2025 day 2 part 1
def check_invalid(number):
    number_len = len(number)
    factors_of_len = []
    for i in range(1, number_len):
        if number_len % i == 0:
            factors_of_len.append(i)
    
    output = False
    for factor in factors_of_len:
        if factor == (len(number)/2):
            # check if the digits from [0:factor] repeat to make the entire string
            segment = number[0:factor]
            repeated_segment = segment * (number_len // factor)
            if repeated_segment == number:
                output = True
                break

    return output

input_lines = []
with open("input.txt", "r") as f:
    for line in f:
        input_lines.append(line.strip())

in_ = input_lines[0]
groups = in_.split(",")
sum_invalid = 0
for group in groups:
    start_range = group.split("-")[0]
    end_range = group.split("-")[1]


    print(f"Checking range {start_range} to {end_range}")

    for number in range(int(start_range), int(end_range) + 1):
        number_str = str(number)
        if check_invalid(number_str):
            print(f"Invalid number found: {number}")
            sum_invalid += number 

print(sum_invalid)