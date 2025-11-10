auta = [
    {
        "marka": "Audi",
        "model": "a6",
        "moc": 150,
        "przebieg": 90000,
        "wlaczone": False
    },
    {
        "marka": "BMW",
        "model": "X6",
        "moc": 300,
        "przebieg": 80000,
        "wlaczone": False
    }
]


def wlacz_silnik(auto):
    if auto.get("wlaczone"):
        print("Wlaczony!")
    else:
        auto["wlaczone"] = True


marka_auta = input("Podaj marke: ")

for auto in auta:
    if auto.get("marka") == marka_auta:
        wlacz_silnik(auto)


class Auto:
    # self to taki konstruktor
    def __init__(self, marka, model, moc, przebieg, wlaczone):
        self.marka = marka
        self.model = model
        self.moc = moc
        self.przebieg = przebieg
        self.wlaczone = wlaczone

    def __str__(self):
        return f"Auto {self.marka}, {self.model}, o mocy {self.moc}, przebiegu {self.przebieg}, czy silnik wlaczony {self.wlaczone}"


def wlacz_silnik(self):
    if self.wlaczone:
        print("Wlaczony!")
    else: self.wlaczone =True
    print("Wlaczamy silnik!")


auta = Auto(marka="audi", model="A5", moc=150, przebieg=80000, wlaczone=True)
print(auto)
