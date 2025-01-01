# TODO : Writing a simple random emoji generator in python

import emoji
import random


def get_random_emoji(name):
    all_emojis = emoji.EMOJI_DATA
    matching_emojis = [e for e in all_emojis if name in e.lower()]

    if matching_emojis:

        return random.choice(matching_emojis)
    else:
        return random.choice(list(all_emojis.keys()))


# user_input
emoji_input = input("Enter a keyword for emoji :")
result = get_random_emoji(emoji_input)

print(f"The random emoji for '{emoji_input}' is : {result}")
