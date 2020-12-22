from linkedlist import LinkedList

class RollingHash:
    def __init__(self, m, initialValue):
        self.m = m
        self.totalHash = 0 # Store entire calculated hash value.
        # Store independent hash values for each key.
        self.hashes = self.initialValue(initialValue) 


    def initialValue(self, initialValue):
        print(f'Setting initial value to: {initialValue}') 
        initialValueList = LinkedList(None)
        for c in initialValue:
            cHash = self.hash(c)
            if initialValueList.head.val == None:
                initialValueList.head.val = cHash
                self.totalHash += cHash

            else:
                initialValueList.add(cHash)
                self.totalHash += cHash

        return initialValueList

    # key: Value to be hashed.
    # m: size of array to store value in. 
    def hash(self, key):
        tempHash = 0
        alpha = 26
        
        for i in range(len(key)):
            # New hash function does not take placement in string array into consideration.
            tempHash = tempHash + pow(alpha, 2) * ord(key[i])

        return tempHash

    # Add new key to end of hash.
    def append(self, val):
        # The oldHeadHash is 0 when we first start.
        oldHeadHash = 0

        if self.hashes is None:
            self.hashes = LinkedList(self.hash(val))
        else:
            # Delete old head and get old head value for hash.
            oldHeadHash = self.hashes.decapitate()

        # Add the new one.
        newHash = self.hash(val) 
        self.hashes.add(newHash)

        # Recalculate the hash. O(N)
        self.totalHash = self.totalHash - oldHeadHash + newHash

def bruteCheck(a, b):
    print(f'Compare {a} vs {b}')
    match = True 
    for i in range(len(a) - 1):
        if a[i] != b[i]:
            match = False
            break
        
    return match

subString = 'nachos'
bigString = 'fartnutssylikegadgetnachosheismybestfriend'
matchLocation = None
rollingHash = RollingHash(len(subString), bigString[0:len(subString)])

# Get a hash value for  our subString.
subStringRollingHash = RollingHash(len(subString), subString)
subStringHash = subStringRollingHash.totalHash 
print(f'Substring hash is {subStringHash}')
print(f'RollingHash is: {rollingHash.totalHash}')

if subStringHash == rollingHash.totalHash:
    bruteCheck(subString, bigString[0:len(subString)])

else:
    for i in range(len(subString), len(bigString) - len(subString)):
        rollingHash.append(bigString[i])
        print(f'*** i is {i}')
        if rollingHash.totalHash == subStringHash and bruteCheck(subString, bigString[i - len(subString) + 1:i+1]):
            print(f'rollingHash: {rollingHash.totalHash} == {subStringHash} at i: {i}')
            matchLocation = i
            break
