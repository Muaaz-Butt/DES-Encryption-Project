class DESKeyScheduler:
    PC_1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

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

    SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    @staticmethod
    def apply_pc1(key):
        if len(key) != 64:
            raise ValueError("Key must be 64 bits")
        return ''.join(key[i-1] for i in DESKeyScheduler.PC_1)

    @staticmethod
    def left_circular_shift(key_half, num_shifts):
        return key_half[num_shifts:] + key_half[:num_shifts]

    @staticmethod
    def apply_pc2(combined_key):
        """Apply PC-2 permutation to generate 48-bit round key."""
        return ''.join(combined_key[i-1] for i in DESKeyScheduler.PC_2)

    @staticmethod
    def generate_round_keys(master_key):
        key_56bit = DESKeyScheduler.apply_pc1(master_key)
        
        left_half = key_56bit[:28]
        right_half = key_56bit[28:]
        
        round_keys = []
        
        for shift in DESKeyScheduler.SHIFT_SCHEDULE:
            left_half = DESKeyScheduler.left_circular_shift(left_half, shift)
            right_half = DESKeyScheduler.left_circular_shift(right_half, shift)
            
            combined = left_half + right_half
            round_key = DESKeyScheduler.apply_pc2(combined)
            
            round_keys.append(round_key)
            
        return round_keys
