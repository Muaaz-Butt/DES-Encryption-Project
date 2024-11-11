from master_key_generator import generate_master_key
from initial_permutation import initial_permutation
from split_key import split_key_into_32_bits
from key_scheduling import left_circular_shift, SHIFT_SCHEDULE, generate_round_keys
from text_handling import text_to_binary, pad_binary, divide_into_blocks
from take_input_pdf import input_pdf

def main():
    plaintext = input_pdf()
    
    binary_text = text_to_binary(plaintext)
    padded_binary_text = pad_binary(binary_text)
    blocks = divide_into_blocks(padded_binary_text)

    #print(f"Binary text: {binary_text}")
    #print(f"Padded binary text: {padded_binary_text}")
    print(f"64-bit blocks: {blocks}")
    
    name = "MUAAZBUTT"
    master_key = generate_master_key(name)
    #print(f"Generated Master Key: {master_key}")
    
    permutated_key = initial_permutation(master_key)
    #print(f"Permuted Master Key: {permutated_key}")
    
    left_half, right_half = split_key_into_32_bits(permutated_key)
    #print(f"Left Half: {left_half}")
    #print(f"Right Half: {right_half}")
    
    round_keys = generate_round_keys(master_key)
    #print("\nGenerated Round Keys:")
    #for i, round_key in enumerate(round_keys):
        #print(f"Round {i+1} Key: {round_key}")

if __name__ == "__main__":
    main()
