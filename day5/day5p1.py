ingredient_ranges = []
available_ids = []

parsing_ids = False

with open("input.txt", "r") as f:
    for line in f:
        str_val = line.strip()
        if str_val == '':
            parsing_ids = True
            continue
        if parsing_ids == False:
            ingredient_ranges.append(line.strip())
        else:
            available_ids.append(line.strip())

tup_start_end = []
for r in ingredient_ranges:
    ingredient_ranges_split = r.split('-')
    start_idx = int(ingredient_ranges_split[0])
    end_idx = int(ingredient_ranges_split[1])
    tup_start_end.append((start_idx,end_idx))

n_fresh = 0
for id in available_ids:
    added_to_fresh = False
    for item in tup_start_end:
        if int(id) >= item[0] and int(id) <= item[1] and not added_to_fresh:
            n_fresh += 1
            print(id)
            added_to_fresh=True
print(f"n_fresh: {n_fresh}")
