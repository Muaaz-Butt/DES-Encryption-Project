def split_key_into_32_bits(key_64bits):
    left_half = key_64bits[:32]
    right_half = key_64bits[32:]
    
    return left_half, right_half