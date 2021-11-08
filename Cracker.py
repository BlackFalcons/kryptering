from Encryption import Encryption


class Cracker:
    def __init__(self, message, alphabet):
        self.message = message
        self.alphabet = alphabet

    def bruteforce(self):
        for key in range(29):
            print("Using key:" + str(key))
            print(Encryption.decrypt(self.message, key))
