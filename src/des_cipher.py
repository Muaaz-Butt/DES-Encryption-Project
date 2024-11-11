from constants import DESConstants
from key_scheduling import DESKeyScheduler
from text_handling import text_to_binary, pad_binary, divide_into_blocks
from fiestel import FeistelNetwork


class DESCipher:
    def __init__(self, key):
        """Initialize DES cipher with a key."""
        if len(key) != 64:
            raise ValueError("Key must be 64 bits")
        self.round_keys = DESKeyScheduler.generate_round_keys(key)

    def _process_block(self, block, round_keys):
        """Process a single block (used for both encryption and decryption)."""
        # Initial permutation
        block = ''.join(block[i-1] for i in DESConstants.IP)
        
        left = block[:32]
        right = block[32:]
        
        for round_key in round_keys:
            # Save previous right half
            previous_right = right
            
            f_result = FeistelNetwork.f_function(right, round_key)
            
            # XOR left half with f_result
            right = ''.join(str(int(a) ^ int(b)) for a, b in zip(left, f_result))
            
            # Previous right becomes new left
            left = previous_right
        
        # Final block is reverse of last round (right + left)
        final_block = right + left
        
        # Apply final permutation
        return ''.join(final_block[i-1] for i in DESConstants.IP_INVERSE)

    def encrypt_block(self, block):
        """Encrypt a single 64-bit block."""
        return self._process_block(block, self.round_keys)

    def decrypt_block(self, block):
        """Decrypt a single 64-bit block."""
        # Use round keys in reverse order for decryption
        return self._process_block(block, reversed(self.round_keys))

    def encrypt(self, plaintext):
        """Encrypt the entire plaintext."""
        binary_text = text_to_binary(plaintext)
        padded_text = pad_binary(binary_text)
        blocks = divide_into_blocks(padded_text)
        
        return ''.join(self.encrypt_block(block) for block in blocks)

    def decrypt(self, ciphertext):
        """Decrypt the entire ciphertext."""
        if len(ciphertext) % 64 != 0:
            raise ValueError("Ciphertext length must be multiple of 64 bits")
            
        blocks = divide_into_blocks(ciphertext)
        binary_text = ''.join(self.decrypt_block(block) for block in blocks)
        
        # Convert binary back to text
        text = ""
        for i in range(0, len(binary_text), 8):
            byte = binary_text[i:i+8]
            text += chr(int(byte, 2))
        # Remove padding
        while text and text[-1] == '\0':
            text = text[:-1]
            
        return text