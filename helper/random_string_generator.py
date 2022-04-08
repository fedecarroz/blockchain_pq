import random
import string


def get_random_string(length) -> str:
    allowed_characters = string.ascii_letters + string.digits
    rnd_str = "".join(random.choice(allowed_characters) for i in range(length))
    return rnd_str
