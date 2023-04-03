import os
import hmac
import hashlib


def hash_dni(dni):
    key = bytes(os.environ['SECRET_KEY'], 'utf-8')
    byte_dni = bytes(dni, 'utf-8')

    hashed_dni = hmac.new(
        key, byte_dni, hashlib.sha256
    ).hexdigest()
    return hashed_dni
