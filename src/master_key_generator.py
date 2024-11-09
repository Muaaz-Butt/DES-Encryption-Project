def generate_master_key(name):
    # Convert the name to uppercase and remove spaces
    name = name.replace(" ", "").upper()[:8]
    
    # Convert each character to ASCII and convert to binary (8-bit)
    binary_key = ""
    
    for char in name:
        ascii_number = ord(char)
        #print(ascii_number)
        binary_value = format(ascii_number, '08b')
        #print(binary_value)
        binary_key += binary_value
  
    return binary_key
        
    
    