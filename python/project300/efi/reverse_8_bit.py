def reverseBinary(x: int) -> int: 
    # We are going to do this with a 2 bit lookup table.
    r = {0: 0, 1:2, 2: 1, 3: 3}

    # Because we have a 2 bit lookup table, that also means that our mask should be 2 bits as well.
    mask = 3

    # Our mask size will be 2 bits.
    mask_size = 2

    return (r[x >> (mask_size * 3) & mask] | r[x >> (2 * mask_size) & mask] << mask_size | r[x >> mask_size & mask] | r[x & mask] << (mask_size * 3))

print(bin(reverseBinary(147)))