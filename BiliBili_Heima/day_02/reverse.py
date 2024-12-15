# 继承子类的成员函数和变量
class Phone:
    seq = None
    producer = None

    def call_by_4G(self):
        print("4G")


class Phone2(Phone):
    face_id = "10001"

    def call_by_5G(self):
        print("5G")


class NFC:
    nfc_type = "NFC"
    data = 50

    def read_NFC(self):
        print("Reading NFC data")

    def write_NFC(self):
        print("Writing NFC data")


class MyPhone(Phone, NFC):
    pass


myphone = MyPhone()
myphone.call_by_4G()
myphone.read_NFC()
myphone.write_NFC()

# phone = Phone2()
# phone.call_by_4G()
# phone.call_by_5G()
