class Counter:
    def __init__(self, skipEvery = 1):
        self.skipEvery = skipEvery

    def countTo(self, end):
        for i in range(0, end + 1, self.skipEvery):
            print(i) 

    def returnFirstLastCapital(self, firstName, lastName):
        return firstName.upper(), lastName.upper()
c = Counter(2)
c.countTo(100)

first, last = c.returnFirstLastCapital("vince", "martin")
print(f'Hello {first} {last}!')
print(f'Sorted {sorted(first)} {sorted(last)}!')
