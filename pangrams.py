# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

# Example
import string


input_1 = 'We promptly judged antique ivory buckles for the next prize'

input_2 = 'We promptly judged antique ivory buckles for the prize'

# The string contains all letters in the English alphabet, so return pangram.

# Function Description

# Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)


def pangrams(s):
    for char in alphabet_list:
        if char not in s.lower():
            return 'not pangram'
    return 'pangram'


print(pangrams(input_1))
print(pangrams(input_2))