# Päev 1/100

# Kuna progeringis jäi OOP veidi segaseks, otsustasin selle iseseisvalt üle vaadata
# Teen mingit loomade asja siin OOP-iga

# kohati maha vehitud lehelt https://realpython.com/python3-object-oriented-programming/

# Pm esialgne idee on teha siia korralik loomaaed valmis (elevandid, kaelkirjakud, kanad, pardid, papagoid, misiganes)
# Ja neid kuidagi sorteerida??
# Idea pending, mis nendega peale hakata, we'll see

class Loom():
    
    def __init__(self, nimi, vanus, liik):
        self.nimi = nimi
        self.vanus = vanus
        self.liik = liik
        
    def karju(self, heli):
        return "{} on {} ja teeb '{}'.".format(self.nimi, self.liik, heli)

def main():
    
    part = Loom("Jasper", 55, "part")
    print(part.karju("AAAAA"))
    
    tiiger = Loom("Donk", 65, "tiiger")
    print(tiiger.karju("honk"))
    
main()

# Tegelesin lugemise ja veidi ka testimisega. Ja nii on.