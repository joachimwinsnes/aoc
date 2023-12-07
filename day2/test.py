maxes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def is_possible(color_pairs):
    for pair_string in color_pairs:
        [n, color] = pair_string.split(" ")
        if color not in maxes:
            return False
        if int(n) > maxes[color]:
            return False
    return True

with open("input.txt") as f:
    sum_ids = 0
    power_sum = 0
    for line in f:
        [preamble, data] = line.strip().split(": ")
        game_id = int(preamble.split(" ")[1])
        game_is_possible = True
        max_seen = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for game_round in data.split("; "):
            colors = game_round.split(", ")
            if not is_possible(colors):
                game_is_possible = False
                
            for pair in colors:
                [n, color] = pair.split(" ")
                max_seen[color] = max(max_seen[color], int(n))
        if game_is_possible:
            sum_ids += game_id
        else:
            print(game_id)
        power = product([max_seen[key] for key in max_seen])
        power_sum += power
    print("PART 1 " + str(sum_ids))
    print("PART 2 " + str(power_sum))