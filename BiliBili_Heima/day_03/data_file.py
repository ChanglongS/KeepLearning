class Record:
    def __init__(self, data, order_id, money, tel):
        self.data = data
        self.order_id = order_id
        self.money = money
        self.tel = tel

    def __str__(self):
        return f"{self.data}, {self.order_id}, {self.money}, {self.tel}"
