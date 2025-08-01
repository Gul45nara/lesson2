from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23", "+79098765432"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79112233445"),
    Smartphone("Google", "Pixel 7", "+79057654321"),
    Smartphone("OnePlus", "11 Pro", "+79165556677")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
