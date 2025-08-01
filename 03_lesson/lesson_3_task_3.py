from address import Address
from mailing import Mailing


to_address = Address("101000", "Москва", "ул. Тверская", "25", "12")
from_address = Address("190000", "Санкт-Петербург", "Невский пр.", "42", "34")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.50,
    track="RA123456789RU"
)

output = (
    f"Отправление {mailing.track} из "
    f"{from_address.index}, {from_address.city}, "
    f"{from_address.street}, {from_address.house} - "
    f"{from_address.apartment} в {to_address.index}, "
    f"{to_address.city}, {to_address.street}, "
    f"{to_address.house} - {to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)

print(output)
