def getParitySlow(n: int) -> int:
    count = 0

    # Count the bits one at a time!
    while n > 0:
        count += (n & 1)
        n >>= 1

    # An even number of set bits means we have an even parity.
    if count % 2 == 0:
        return 0
    else:
        return 1

def getParityLookup(n: int) -> int:
    # Now we have a lookup table that lets us quickly look up 4 bits at a time.
    # We are trading space for processing time.
    table = {0:0, 1:1, 2:0, 3:1,
            4:0, 5:1, 6:0, 7:1,
            8:1, 9:0, 10:0, 11:1,
            12:0, 13:1, 14:1, 15:0}

    # We are going to use a 4 bit mask.
    mask = int('1111', 2)

    # Store parity.
    parity = 0

    # Process n
    while n > 0:
        parity ^= table[n & mask]
        n >>= 4

    return parity


# Lets test this thing.
#print(f'Get 4 slow: {getParitySlow(4)}')
#print(f'Get 3 slow: {getParitySlow(3)}')

print(f'Get 255 lookup: {getParityLookup(255)}')
print(f'Get 254 lookup: {getParityLookup(254)}')