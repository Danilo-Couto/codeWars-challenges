# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

# Example:
# s = 'middle-Outz'
# k = 2
s = 'Hello_World!'
k = 4

import string


def caesarCipher(s, k):
    alpha = string.ascii_lowercase
    a_len = len(alpha)
    new_word = ''

    for c in s:
        if c.isalpha():
            a_i = alpha.index(c.lower()) + k % 26
            if c.isupper():
                new_word += (alpha[a_i-a_len].strip()).upper()
            else:
                new_word += alpha[a_i-a_len].strip()
        else:
            new_word += c

    return new_word

        
print(caesarCipher(s, k))