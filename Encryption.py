from string import ascii_lowercase, ascii_uppercase


class Encryption:
    @staticmethod
    def shuffle(s, key):
        key %= len(s)
        return s[key:] + s[:key]

    @staticmethod
    def createKey(from_alphabet, to_alphabet):
        d = {}
        for i in range(len(from_alphabet)):
            d[from_alphabet[i]] = to_alphabet[i]
        return d

    @staticmethod
    def getEncryptionDict(key):
        norwegian_ascii_letters = ascii_lowercase + "æøå" + ascii_uppercase + "ÆØÅ"
        norwegian_ascii_letters_shuffeled = Encryption.shuffle(ascii_lowercase + "æøå", key) + Encryption.shuffle(
            ascii_uppercase + "ÆØÅ", key)
        return Encryption.createKey(norwegian_ascii_letters, norwegian_ascii_letters_shuffeled)

    @staticmethod
    def getDecryptionDict(key):
        norwegian_ascii_letters = ascii_lowercase + "æøå" + ascii_uppercase + "ÆØÅ"
        norwegian_ascii_letters_shuffeled = Encryption.shuffle(ascii_lowercase + "æøå", key) + Encryption.shuffle(
            ascii_uppercase + "ÆØÅ", key)
        return Encryption.createKey(norwegian_ascii_letters_shuffeled, norwegian_ascii_letters)

    @staticmethod
    def encrypt(message, key, remove_missing=False):
        final_message = ""
        encryption_dict = Encryption.getEncryptionDict(key)

        for char in message:
            try:
                final_message += encryption_dict[char]
            except KeyError:
                if remove_missing:
                    pass
                else:
                    final_message += char
        return final_message

    @staticmethod
    def decrypt(message, key, remove_missing=False):
        final_message = ""
        encryption_dict = Encryption.getDecryptionDict(key)

        for char in message:
            try:
                final_message += encryption_dict[char]
            except KeyError:
                if remove_missing:
                    pass
                else:
                    final_message += char
        return final_message
