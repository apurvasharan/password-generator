#!/usr/bin/env python3

import random

NUMBERS = "123456789"
CHARACTERS = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
SPECIAL_CHARS = "!@#$%^*"

password = []
password.extend(random.sample(NUMBERS, 1))
password.extend(random.sample(SPECIAL_CHARS, 1))
password.extend(random.sample(CHARACTERS, 6))
random.shuffle(password)
print("".join(password))

