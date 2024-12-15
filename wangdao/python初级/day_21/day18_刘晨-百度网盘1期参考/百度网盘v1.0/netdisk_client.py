# create by liuchen 2022/3/5 10:08
import socket
import struct
import os


class Client:
    main_path = os.getcwd()

    def __init__(self):
        self.sock = None
        pass

    def connect_server(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((ip, port))

    def send_packed_bytes(self, content):
        len_content_bytes = struct.pack('I', len(content.encode('utf8')))
        self.sock.send(len_content_bytes + content.encode('utf8'))

    def recv_packed_bytes(self):
        len_bytes = self.sock.recv(4)
        try:
            rec = self.sock.recv(struct.unpack('I', len_bytes)[0])
        except:
            return
        else:
            return rec

    def send_big_file(self, file):
        try:
            fd = open(file, 'rb')
        except FileNotFoundError:
            print('文件不存在')
        else:
            self.send_packed_bytes(file)
            total_size = os.stat(file).st_size
            total_bytes = struct.pack('I', total_size)
            tmp_size = total_size
            self.sock.send(total_bytes)
            while tmp_size > 0:
                content = fd.read(1024)
                self.sock.send(content)
                tmp_size -= 1024
            fd.close()

    def recv_big_file(self):
        os.chdir(Client.main_path + '/local')
        file_name = self.recv_packed_bytes().decode('utf8')
        fd = open(file_name, 'wb')
        total_bytes = self.sock.recv(4)
        total_size = struct.unpack('I', total_bytes)[0]
        tmp_size = total_size
        while tmp_size > 0:
            content = self.sock.recv(1024)
            fd.write(content)
            tmp_size -= 1024
        fd.close()

    @staticmethod
    def show_file_detail(file_path):
        file_detail = ''
        os.chdir(file_path)
        for file in os.listdir(file_path):
            file_detail += file.ljust(20) + '\t' + \
                           str(os.stat(file).st_size).ljust(10) + '\n'
        print(file_detail)

    def log_in(self):
        while True:
            user_name = input(self.recv_packed_bytes().decode('utf8'))
            self.send_packed_bytes(user_name)
            passwd = input(self.recv_packed_bytes().decode('utf8'))
            self.send_packed_bytes(passwd)
            flag = self.recv_packed_bytes().decode('utf8')
            if flag == 'success':
                break
            else:
                print(flag)

    def send_command(self):
        while True:
            command = input()
            self.send_packed_bytes(command)
            if command[:2] == 'ls':
                self.op_ls()
            elif command[:2] == 'cd':
                self.op_cd()
            elif command[:2] == 'rm':
                self.op_rm()
            elif command[:3] == 'pwd':
                self.op_pwd()
            elif command[:4] == 'gets':
                self.op_gets()
            elif command[:4] == 'puts':
                self.op_puts()

    def op_ls(self):
        # self.send_packed_bytes('ls')
        reply = self.recv_packed_bytes()
        print(reply.decode('utf8'))

    def op_cd(self):
        reply = self.recv_packed_bytes()
        print(reply.decode('utf8'))

    def op_rm(self):
        reply = self.recv_packed_bytes()
        print(reply.decode('utf8'))

    def op_pwd(self):
        reply = self.recv_packed_bytes()
        print(reply.decode('utf8'))

    def op_gets(self):
        file_detail = self.recv_packed_bytes()
        print(file_detail.decode('utf8'))
        file_name = input('请输入要下载的文件名')
        self.send_packed_bytes(file_name)
        rec = self.recv_packed_bytes().decode('utf8')
        if rec == '0':
            print('文件不存在')
        else:
            self.recv_big_file()
            print('下载成功！')

    def op_puts(self):
        Client.show_file_detail(Client.main_path + '/local')
        file = input('请输入要上传的文件名')
        self.send_big_file(file)
        print(self.recv_packed_bytes().decode('utf8'))


if __name__ == '__main__':
    client = Client()
    client.connect_server('192.168.159.1', 2333)
    client.log_in()
    client.send_command()
