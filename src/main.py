from master_key_generator import generate_master_key
from initial_permutation import initial_permutation
from split_key import split_key_into_32_bits
from key_scheduling import DESKeyScheduler
from text_handling import text_to_binary, pad_binary, divide_into_blocks
from take_input_pdf import input_pdf
from des_cipher import DESCipher

def main():
    try:
        print("Reading PDF file...")
        plaintext = input_pdf()
        print(f"Successfully extracted text ({len(plaintext)} characters)")
        
        name = "MUAAZBUT"
        master_key = generate_master_key(name)
        print("Master key generated successfully")
        
        # Create DES cipher instance
        des = DESCipher(master_key)
        
        # Encrypt the text
        print("\nEncrypting text...")
        ciphertext = des.encrypt(plaintext)
        print("Encryption successful!")
        print(f"\nFirst 64 bits of ciphertext: {ciphertext[:64]}")
        
        # Decrypt the text
        print("\nDecrypting text...")
        decrypted_text = des.decrypt(ciphertext)
        print("Decryption successful!")
        
        # Verify results
        if decrypted_text == plaintext:
            print("\nVerification successful: Decrypted text matches original!")
        else:
            print("\nWarning: Decrypted text differs from original!")
            
        # Save results
        with open("encrypted.txt", "w") as f:
            f.write(ciphertext)
        with open("decrypted.txt", "w") as f:
            f.write(decrypted_text)
            
        print("\nResults have been saved to 'encrypted.txt' and 'decrypted.txt'")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()