import hashlib
import os
import getpass

haslo = 0

def generate_secure_credentials():
    print("--- Generator Bezpiecznego Klucza z Solą ---")
    password = getpass.getpass("Wpisz swoje tajne hasło: ")
    
    # Generujemy losową sól (16 bajtów)
    salt = os.urandom(16).hex()
    
    # Łączymy hasło z solą i hashujemy
    salted_password = password + salt
    final_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    
    print("\nGotowe! Skopiuj te dwa parametry do swojego kodu:")
    print(f"SALT = '{salt}'")
    print(f"STORED_HASH = '{final_hash}'")



class SecureProgressGuard:
    def __init__(self):
        # Te wartości wklejasz z generatora powyżej
        self.salt = "salt"
        self.stored_hash = "hash"

    def verify_access(self, input_password):
        combined = input_password + self.salt
        input_hash = hashlib.sha256(combined.encode()).hexdigest()
        
        return input_hash == self.stored_hash




if __name__ == "__main__":
    if haslo == 0:
        generate_secure_credentials()
    guard = SecureProgressGuard()
    if guard.verify_access(input()):
        print("brawo")
