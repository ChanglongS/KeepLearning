class Phone:
    producer = "1"

    def call_by_5G(self):
        print("5G--1")


class Phone2(Phone):
    producer = "2"

    def call_by_5G(self):
        print("5G--2")
        print(f"Phone2 producer is {self.producer}")
        print(f"Phone producer is {Phone.producer}")
        print(f"Phone producer is {super().producer}")
        Phone.call_by_5G(self)
        super().call_by_5G()


phone = Phone2()
phone.call_by_5G()
