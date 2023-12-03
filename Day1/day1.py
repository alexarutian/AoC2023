input_file = "day1.txt"
inputs = []
with open(input_file) as file:
    for line in file:
        inputs.append(line)

# part 1
# for each line of input file
# combine the first digit with the last digit to form a two-digit number
# sum all the numbers together to get the 'calibration' total

calibration_total = 0

for line in inputs:
    # get all digits in line
    line = line.strip()
    digits = []
    for letter in line:
        if letter.isdigit():
            digits.append(int(letter))

    # handle situation where number of digits is 2 or greater
    if len(digits) > 1:
        first_value = digits[0]
        last_value = digits[len(digits) - 1]

    # handle situation where number of digits is 1
    else:
        first_value = digits[0]
        last_value = digits[0]

    # compile two numbers into two digit number
    calibration_value = first_value * 10 + last_value

    # add to running total
    calibration_total += calibration_value

print(f"calibration_total for part 1: {calibration_total}")


# part 2
# count parts of string that spell out numbers e.g. 'eight' 'one'
number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

calibration_total_2 = 0

for line in inputs:
    line = line.strip()

    # format = {index: number}
    numbers_location_map = {}

    # first find the spelled out letters
    for n in number_map.keys():
        keep_looking = True
        start_idx = 0

        while keep_looking:
            index = line.find(n, start_idx)
            if index == -1:
                keep_looking = False
            else:
                start_idx = index + 1
                numbers_location_map[index] = number_map[n]

    
    for idx, letter in enumerate(line):
        if letter.isdigit():
            numbers_location_map[idx] = int(letter)
        

    # sort the map by its keys
    sorted_dict = dict(sorted(numbers_location_map.items()))

    # keep only the values
    digits = list(sorted_dict.values())

    # handle situation where number of digits is 2 or greater
    if len(digits) > 1:
        first_value = digits[0]
        last_value = digits[len(digits) - 1]

    # handle situation where number of digits is 1
    else:
        first_value = digits[0]
        last_value = digits[0]

    # compile two numbers into two digit number
    calibration_value = first_value * 10 + last_value
    print(calibration_value)

    # add to running total
    calibration_total_2 += calibration_value

print(f"calibration_total for part 2: {calibration_total_2}")
