class Property:
    def __init__(self, area, rooms, price, address, data_publikacji):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.data_publikacji = data_publikacji

    def __str__(self):
        return (
            f"Nieruchomość: Adres: {self.address}, Powierzchnia: {self.area} m², "
            f"Pokoje: {self.rooms}, Cena: {self.price} PLN, Data: {self.data_publikacji}"
        )


class House(Property):
    def __init__(self, area, rooms, price, address, plot, data_publikacji):
        super().__init__(area, rooms, price, address, data_publikacji)
        self.plot = plot

    def __str__(self):
        return (
            f"DOM: Adres: {self.address}, Powierzchnia: {self.area} m², "
            f"Pokoje: {self.rooms}, Cena: {self.price} PLN, "
            f"Działka: {self.plot} m²,"
            f"Data publikacji: {self.data_publikacji}"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor, data_publikacji):
        super().__init__(area, rooms, price, address, data_publikacji)
        self.floor = floor

    def __str__(self):
        return (
            f"MIESZKANIE: Adres: {self.address}, "
            f"Powierzchnia: {self.area} m², "
            f"Pokoje: {self.rooms}, Cena: {self.price} PLN, "
            f"Piętro: {self.floor},"
            f"Data publikacji: {self.data_publikacji}"
        )


dom_na_wsi = House(
    area=80,
    rooms=4,
    price=500000,
    address="ul. Kołakowa 22, 21-231 Katowice",
    plot=266,
    data_publikacji="22/02/2025",
)


mieszkanie_chorzow = Flat(
    area=37.0,
    rooms=2,
    price=230000,
    address="ul. Brzozowa 30/5, 41-500 Chorzów",
    floor=2,
    data_publikacji="22/04/2025",
)


print(dom_na_wsi)
print(mieszkanie_chorzow)
