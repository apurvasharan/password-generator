#!/usr/bin/env python3

import random

NUMBERS = "123456789"
CHARACTERS = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
SPECIAL_CHARS = "!@#$%^*"

def permute_random(data):
    permutation = []
    while (len(data) > 0):
        if len(data) == 1:
            permutation.append(data[0])
            data = ""
        else:
            p = random.sample(range(len(data)), 1)[0]
            permutation.append(data[p])
            if (p != 0) and (p != len(data) - 1):
                temp_data = data[0:p]
                temp_data.extend(data[p+1:])
                data = temp_data
            elif p == 0:
                data = data[1:]
            else:
                data = data[:-1] 
    return permutation

password_chars = []
password_chars.extend(random.sample(NUMBERS, 1))
password_chars.extend(random.sample(SPECIAL_CHARS, 1))
password_chars.extend(random.sample(CHARACTERS, 6))
password = permute_random(password_chars)
print("".join(password))

