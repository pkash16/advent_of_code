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

def find_collision(startend1, startend2):
    start_idx1, end_idx1 = startend1
    start_idx2, end_idx2 = startend2
    if start_idx2 <= end_idx1 and start_idx2 >= start_idx1:
        return True
    if end_idx2 >= start_idx1 and start_idx2 <= start_idx1:
        return True
    return False

def resolve_collision_pass(start_end_list):
    idx_to_del = [] 
    for idx, item in enumerate(start_end_list):
        for idx2 in range(idx+1, len(start_end_list)):
            item2 = start_end_list[idx2] 
            # we are looking for collisions 
            if find_collision(item, item2):
                print(f"found collision between {item}, {item2}")
                resolved = (min(item[0], item2[0]), max(item[1], item2[1]))
                start_end_list[idx2] = resolved
                idx_to_del.append(idx)
                print(start_end_list)
                break
    print(len(idx_to_del))
    if len(idx_to_del) == 0:
        return start_end_list, True 
    print(idx_to_del)

    start_end_copy = []
    for item in range(len(start_end_list)):
        if item not in idx_to_del:
            start_end_copy.append(start_end_list[item])
    
    return start_end_copy, False

running = True
while running:
    tup_start_end, notrun = resolve_collision_pass(tup_start_end)
    running = not notrun

print(tup_start_end)

running_sum = 0
for item in tup_start_end:
    running_sum += item[1] - item[0] + 1

print(running_sum)