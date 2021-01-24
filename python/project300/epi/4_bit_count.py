def count_bits(x: int) -> int:
    num_bits = 0

    while x:
        print(f'num_bits: {num_bits} x: {x}')
        num_bits += x & 1
        x >>= 1
        

    return num_bits

print(count_bits(12))
