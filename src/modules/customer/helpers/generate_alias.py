import random
import string


def generate_alias(name) -> str:
    prefix = 'neobank'
    randomcaracteres = ''.join(random.choice(
        string.ascii_letters) for _ in range(3))
    alias = f'{prefix}_{name}_{randomcaracteres}'

    return alias
