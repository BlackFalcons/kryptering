from Encryption import Encryption


class Cracker:
    def __init__(self, message, alphabet):
        self.message = message
        self.alphabet = alphabet

    def getResult(self):
        print(self.message)
        print(self.alphabet)
        for key in range(29):
            print("Using key:" + str(1 + key - 1))
            print(Encryption.decrypt(self.message, key))
