def square_and_multiply(a, b, n):
    # Convert exponent b to its binary representation (as a string)
    binary_b = bin(b)[2:]
    c = 0
    f = 1
    
    # Define header and separator
    header = f"{'Iteration':>9} | {'Bit':>3} | {'c':>5} | {'f':>5}"
    print(header)
    print("-" * len(header))
    
    # Process each bit (from MSB to LSB)
    for i, bit in enumerate(binary_b, start=1):
        # Print the current iteration's state before processing the bit
        print(f"{i:9d} | {bit:>3} | {c:5d} | {f:5d}")
        
        # Square c and f (mod n for f)
        c = 2 * c
        f = (f * f) % n
        
        # If the current bit is '1', update c and f accordingly
        if bit == '1':
            c += 1
            f = (f * a) % n
        
        # Print the updated state after processing the bit
        print(f"After {i:2d} |       | {c:5d} | {f:5d}\n")
    
    return f

# Example usage: compute 5^596 mod 1234
a = 5
b = 596
n = 1234
result = square_and_multiply(a, b, n)
print("Final result:")
print(f"{a}^{b} mod {n} = {result}")

