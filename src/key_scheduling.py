from initial_permutation import initial_permutation
from split_key import split_key_into_32_bits

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 
                  1, 2, 2, 2, 2, 2, 2, 1]

def left_circular_shift(key_half, num_shifts):
    shifted = key_half[num_shifts:] + key_half[:num_shifts]
    return shifted
  
PC_2 = [
    14, 17, 11, 24, 1, 5, 
    3, 28, 15, 6, 21, 10, 
    23, 19, 12, 4, 26, 8, 
    16, 7, 27, 20, 13, 2, 
    41, 52, 31, 37, 47, 55, 
    30, 40, 51, 45, 33, 48, 
    44, 49, 39, 56, 34, 53, 
    46, 42, 50, 36, 29, 32
]

def apply_pc2_permutation(left_half, right_half): 
    combined_key = left_half + right_half

    round_key = ''.join(combined_key[i - 1] for i in PC_2)
    return round_key


def generate_round_keys(master_key):
    
    round_keys = []

    permuted_key = initial_permutation(master_key)

    left_half, right_half = split_key_into_32_bits(permuted_key)

    for round_number in range(16):
        left_half = left_circular_shift(left_half, SHIFT_SCHEDULE[round_number])
        right_half = left_circular_shift(right_half, SHIFT_SCHEDULE[round_number])

        round_key = apply_pc2_permutation(left_half, right_half)
        round_keys.append(round_key)

    return round_keys
