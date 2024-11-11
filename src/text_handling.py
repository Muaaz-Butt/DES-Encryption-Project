def text_to_binary(text):
    """Convert text to binary string."""
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
        
    if not text:
        raise ValueError("Input text cannot be empty")
        
    return ''.join(format(ord(char), '08b') for char in text)

def pad_binary(binary_string):
    """Pad binary string to multiple of 64 bits."""
    if not isinstance(binary_string, str):
        raise ValueError("Input must be a binary string")
        
    if not all(bit in '01' for bit in binary_string):
        raise ValueError("Input must be a binary string containing only 0s and 1s")
    
    padding_length = (64 - (len(binary_string) % 64)) % 64
    return binary_string.ljust(len(binary_string) + padding_length, '0')

def divide_into_blocks(binary_string):
    """Divide binary string into 64-bit blocks."""
    if not isinstance(binary_string, str):
        raise ValueError("Input must be a binary string")
        
    if len(binary_string) % 64 != 0:
        raise ValueError("Input length must be multiple of 64 bits")
        
    if not all(bit in '01' for bit in binary_string):
        raise ValueError("Input must be a binary string containing only 0s and 1s")
    
    return [binary_string[i:i+64] for i in range(0, len(binary_string), 64)]