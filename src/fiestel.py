from constants import DESConstants
from key_scheduling import DESKeyScheduler

class FeistelNetwork:
    @staticmethod
    def expansion(input_bits):
        """Expand 32 bits to 48 bits using the E-box."""
        return ''.join(input_bits[i-1] for i in DESConstants.EXPANSION)

    @staticmethod
    def substitute(input_48bits):
        """Apply S-box substitution (48 bits -> 32 bits)."""
        output = ""
        for i in range(0, 48, 6):
            block = input_48bits[i:i+6]
            row = int(block[0] + block[5], 2)
            col = int(block[1:5], 2)
            value = DESConstants.S_BOXES[i//6][row][col]
            output += format(value, '04b')
        return output

    @staticmethod
    def permute(input_32bits):
        """Apply P-box permutation."""
        return ''.join(input_32bits[i-1] for i in DESConstants.P_BOX)

    @staticmethod
    def f_function(right_half, round_key):
        """Complete f-function for the Feistel network."""
        # 1. Expansion (32 -> 48 bits)
        expanded = FeistelNetwork.expansion(right_half)
        
        # 2. XOR with round key
        xored = ''.join(str(int(a) ^ int(b)) for a, b in zip(expanded, round_key))
        
        # 3. S-box substitution (48 -> 32 bits)
        substituted = FeistelNetwork.substitute(xored)
        
        # 4. P-box permutation
        permuted = FeistelNetwork.permute(substituted)
        
        return permuted