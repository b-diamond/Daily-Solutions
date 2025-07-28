substring = input()

value_map = [['a', 'b'], ['c', 'd', 'e'], ['f', 'g', 'h'],
             ['i', 'j', 'k'], ['l', 'm', 'n'], ['o', 'p', 'q'],
             ['r', 's', 't'], ['u', 'v', 'w'], ['x', 'y', 'z']]


def letter_value(letter):
    for i, sublist in enumerate(value_map):
        if letter in sublist:
            return i + 1
    else:
        return 0
length_of_substring = len(substring)
substring_value = 0
for char in substring:
    substring_value += letter_value(char)
if substring_value % length_of_substring == 0:
    print(f"Extraordinary Substring Found! {substring}")
else:
    print(f"{substring} is not an Extraordinary Substring")