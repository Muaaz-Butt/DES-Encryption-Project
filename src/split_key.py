def split_key_into_32_bits(key_64bits):
    left_helf = key_64bits[:32]
    right_half = key_64bits[32:]
    
    return left_helf, right_half