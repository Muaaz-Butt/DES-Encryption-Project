def split_key_into_32_bits(key_64bits):
    """Split a 64-bit key into two 32-bit halves."""
    if not isinstance(key_64bits, str):
        raise ValueError("Input must be a binary string")
        
    if len(key_64bits) != 64:
        raise ValueError("Input must be exactly 64 bits")
        
    if not all(bit in '01' for bit in key_64bits):
        raise ValueError("Input must be a binary string containing only 0s and 1s")
    
    return key_64bits[:32], key_64bits[32:]