input_file = "day3.txt"
inputs = []
with open(input_file) as file:
    for line in file:
        inputs.append(line)

# obtain our range of special characters
special_characters = []
for line in inputs:
    for item in line:
        if item not in special_characters and not item.isdigit() and item != "." and item != "\n":
            special_characters.append(item)

print(special_characters)

# this is the output of special_characters
['*', '=', '-', '+', '&', '#', '%', '/', '@', '$']

# need to read previous line as well as current line
# maintain index of any special characters
# deem what is adjacent or diagonal to special characters

# start with all numbers on same line adjacent to special characters
for line in inputs:
    for sc in special_characters:
        index = line.find(sc)
