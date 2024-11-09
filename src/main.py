from master_key_generator import generate_master_key
from initial_permutation import initial_permutation

def main():
    name = "MUAAZBUTT"
    master_key = generate_master_key(name)
    print(f"Generated Master Key: {master_key}")
    
    permutated_key = initial_permutation(master_key)
    print(f"Permuted Master Key: {permutated_key}")
    
if __name__ == "__main__":
    main()