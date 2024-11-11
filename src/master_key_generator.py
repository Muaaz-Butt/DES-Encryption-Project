def generate_master_key(name):
    """Generate a 64-bit key from a name."""
    if not isinstance(name, str):
        raise ValueError("Input must be a string")
    
    name = name.replace(" ", "").upper()
    
    if len(name) < 8:
        name = name.ljust(8, 'X')  
    else:
        name = name[:8]  

    binary_key = ''.join(format(ord(char), '08b') for char in name)
    
    if len(binary_key) != 64:
        raise ValueError("Generated key must be exactly 64 bits")
        
    return binary_key