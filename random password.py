import random
import string


def generate_password(length=12):
    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]
    pool = string.ascii_letters + string.digits
    chars += [random.choice(pool) for _ in range(length - 3)]
    random.shuffle(chars)
    return "".join(chars)


if __name__ == "__main__":
    print(generate_password(16))
