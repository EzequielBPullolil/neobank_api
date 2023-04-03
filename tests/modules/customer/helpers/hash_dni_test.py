from modules.customer.helpers.hash_dni import hash_dni


class TestHashDni:
    def test_hash_the_same_dni_return_same_encription(self):
        '''
            Check if hash the same dni return the same
            hash
        '''
        text = '44444444'
        first_encrypt = encrypt_dni(text)
        seccond_encrypt = encrypt_dni(text)

        assert first_encrypt == seccond_encrypt
