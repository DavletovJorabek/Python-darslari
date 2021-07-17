class Xodim:
    def __init__(self, ismi, manzili, maoshi):
        self.ismi = ismi
        self.manzili = manzili
        self.maoshi = maoshi

def gap(self):


xodimlar = []
x1 = Xodim("Bunyod", "Lalmikor", 4000000)
xodimlar.append(x1)
x2 = Xodim("Sunnat", "Lalmikor", 400000)
xodimlar.append(x2)
x3 = Xodim("Doston", "Lalmikor", 3000000)
xodimlar.append(x3)
x4 = Xodim("Ilyos", "Lalmikor", 1500000)
xodimlar.append(x4)
x5 = Xodim("Shoxzod", "Lalmikor", 9000000)
xodimlar.append(x5)

for xodim in xodimlar:
    if xodim.maoshi < 2000000:
        print("Mening ismim" + " ", xodim.ismi,' ',xodim.gap)