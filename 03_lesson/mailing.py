class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track}:\n"
                f"  От кого: {self.from_address}\n"
                f"  Кому: {self.to_address}\n"
                f"  Стоимость: {self.cost} рублей")
#"Добавлен еще 1 комментарий"