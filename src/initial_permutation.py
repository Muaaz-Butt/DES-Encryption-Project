def initial_permutation(input_key):
    """Perform initial permutation on 64-bit input."""
    if not isinstance(input_key, str):
        raise ValueError("Input must be a binary string")
    
    if len(input_key) != 64:
        raise ValueError("Input must be exactly 64 bits")
        
    if not all(bit in '01' for bit in input_key):
        raise ValueError("Input must be a binary string containing only 0s and 1s")
    
    IP_TABLE = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    
    input_bits = [int(bit) for bit in input_key]
    permuted_bits = [input_bits[i - 1] for i in IP_TABLE]
    return ''.join(str(bit) for bit in permuted_bits)