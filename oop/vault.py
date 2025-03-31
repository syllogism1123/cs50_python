class Vault:
    def __init__(self, galleon=0, sickles=0, knuts=0):
        self.galleon = galleon
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleon} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleon = self.galleon + other.galleon
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleon, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

print(potter + weasley)
