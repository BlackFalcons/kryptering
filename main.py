from Encryption import Encryption

if __name__ == '__main__':
    while True:
        prompt_encryption = input("Vil du kryptere eller dekryptere(krypter eller dekryptere): ")
        prompt_lowered = prompt_encryption.lower()

        if prompt_lowered == "krypter":
            try:
                key = int(input("Oppgi nøkkel: "))
            except ValueError:
                print("You have to provide a integer.")
                break

            msg = input("Skriv inn meldingen: ")

            if isinstance(key, int):
                print(Encryption.encrypt(msg, key))
            else:
                print("Du må oppgi et heltall!")
            break
        elif prompt_lowered == "dekryptere":
            try:
                key = int(input("Oppgi nøkkel: "))
            except ValueError:
                print("You have to provide a integer.")
                break

            msg = input("Skriv inn meldingen: ")

            if isinstance(key, int):
                print(Encryption.decrypt(msg, key))
            else:
                print("Du må oppgi et heltall!")
            break
