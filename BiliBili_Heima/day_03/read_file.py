import json

from data_file import Record


# 抽象类
class ReadFile:
    def read_file(self) -> list[Record]:
        pass


class TextReadFile(ReadFile):
    def __init__(self, path):
        self.path = path

    def read_file(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonReadFile(ReadFile):
    def __init__(self, path):
        self.path = path

    def read_file(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["data"], data_dict["order_id"], data_dict["money"], data_dict["tel"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_data_file = TextReadFile("./data.txt")
    json_data_file = JsonReadFile("./data.json")
    text_data = text_data_file.read_file()
    json_data = json_data_file.read_file()
    print(text_data)
    print(json_data)
