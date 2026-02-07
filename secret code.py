import random
import string

def random_letters(n=3):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def encode(message):
    words = message.split()
    encoded_words = []

    for word in words:
        if len(word) >= 3:
            prefix = random_letters()
            suffix = random_letters()
            new_word = prefix + word[1:] + word[0] + suffix
            encoded_words.append(new_word)
        else:
            encoded_words.append(word[::-1])

    return " ".join(encoded_words)


def decode(message):
    words = message.split()
    decoded_words = []

    for word in words:
        if len(word) >= 3:
            core = word[3:-3]
            original = core[-1] + core[:-1]
            decoded_words.append(original)
        else:
            decoded_words.append(word[::-1])

    return " ".join(decoded_words)


# ----------- Usage -----------
text = input("Enter message: ")

encoded = encode(text)
print("Encoded:", encoded)

decoded = decode(encoded)
print("Decoded:", decoded)
