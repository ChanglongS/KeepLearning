class Clock:
    no = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(500, 500)


clock_1 = Clock()
clock_1.no = 1
clock_1.price = 200
print(f"price is {clock_1.price}, no is {clock_1.no}")
clock_1.ring()
