
def text_to_binary(text):
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string

def pad_binary(binary_string):
    if len(binary_string) % 64 != 0:
        padding_length = 64 - (len(binary_string) % 64)
        binary_string = binary_string.ljust(len(binary_string) + padding_length, '0')
    return binary_string

def divide_into_blocks(binary_string):
    return [binary_string[i:i+64] for i in range(0, len(binary_string), 64)]

if __name__ == "__main__":
    plaintext = "MUAAZBUTHELLO"
    binary_text = text_to_binary(plaintext)
    padded_binary_text = pad_binary(binary_text)
    blocks = divide_into_blocks(padded_binary_text)

    print(f"Binary text: {binary_text}")
    print(f"Padded binary text: {padded_binary_text}")
    print(f"64-bit blocks: {blocks}")
