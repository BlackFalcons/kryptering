from Cracker import Cracker
from Encryption import Encryption

if __name__ == '__main__':
    cracker = Cracker("Imzmrh", Encryption.getNorwegianAlphabet())
    cracker.bruteforce()

    # while True:
    #     prompt_encryption = input("Vil du kryptere eller dekryptere(k eller d): ")
    #     prompt_lowered = prompt_encryption.lower()
    #
    #     if prompt_lowered == "k":
    #         try:
    #             key = int(input("Oppgi nøkkel: "))
    #         except ValueError:
    #             print("You have to provide a integer.")
    #             break
    #
    #         msg = input("Skriv inn meldingen: ")
    #
    #         if isinstance(key, int):
    #             print(Encryption.encrypt(msg, key))
    #         else:
    #             print("Du må oppgi et heltall!")
    #         break
    #     elif prompt_lowered == "d":
    #         try:
    #             key = int(input("Oppgi nøkkel: "))
    #         except ValueError:
    #             print("You have to provide a integer.")
    #             break
    #
    #         msg = input("Skriv inn meldingen: ")
    #
    #         if isinstance(key, int):
    #             print(Encryption.decrypt(msg, key))
    #         else:
    #             print("Du må oppgi et heltall!")
    #         break
