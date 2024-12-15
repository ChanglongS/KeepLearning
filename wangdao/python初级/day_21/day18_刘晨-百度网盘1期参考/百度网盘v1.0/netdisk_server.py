# create by liuchen 2022/3/5 10:09
import socket
import struct
import os
import dbm


class Server:
    main_path = os.getcwd()

    def __init__(self, ip='', port=2333):
        self.sock = None
        self.ip = ip
        self.port = port
        self.account_list = dbm.open('account', 'c')
        # self.user_name_list = set()

    def tcp_init(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(128)

    def start(self):
        new_s, client_addr = self.sock.accept()
        user = User(new_s, client_addr[0], client_addr[1])
        user.account_validate(self.account_list)
        user.create_user_space()
        user.deal_command()
        os.chdir(Server.main_path)

    @staticmethod
    def show_file_detail(file_path):
        file_detail = ''
        os.chdir(file_path)
        for file in os.listdir(file_path):
            file_detail += file.ljust(20) + '\t' + \
                           str(os.stat(file).st_size).ljust(10) + '\n'
        return file_detail


class User:
    def __init__(self, sock, ip, port):
        self.sock: socket.socket = sock
        self.user_name = None
        self.user_passwd = None
        self.ip = ip
        self.port = port
        self.user_path = ''

    def send_packed_bytes(self, content):
        len_content_bytes = struct.pack('I', len(content.encode('utf8')))
        try:
            self.sock.send(len_content_bytes + content.encode('utf8'))
        except:
            return

    def recv_packed_bytes(self):
        try:
            len_bytes = self.sock.recv(4)
        except:
            return
        return self.sock.recv(struct.unpack('I', len_bytes)[0])

    def send_big_file(self, file):
        try:
            fd = open(file, 'rb')
        except FileNotFoundError:
            self.send_packed_bytes('0')
        else:
            self.send_packed_bytes('开始下载')
            self.send_packed_bytes(file)
            total_size = os.stat(file).st_size
            total_bytes = struct.pack('I', total_size)
            tmp_size = total_size
            self.sock.send(total_bytes)
            while tmp_size > 0:
                content = fd.read(1024)
                self.sock.send(content)
                tmp_size -= 1024

    def recv_big_file(self):
        os.chdir(Server.main_path + '/' + self.user_name)
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

    def account_validate(self, account_list):
        while True:
            self.send_packed_bytes('请输入账户名(若不存在将自动创建)：')
            user_name = self.recv_packed_bytes()
            if user_name == None:
                break
            if user_name not in account_list.keys():
                self.send_packed_bytes('请输入密码：')
                passwd = self.recv_packed_bytes().decode('utf8')
                account_list[user_name] = passwd
                print(user_name.decode('utf8'))
                os.mkdir(user_name.decode('utf8'))
                self.send_packed_bytes('success')
                self.user_name = user_name.decode('utf8')
                break
            else:
                self.send_packed_bytes('请输入密码：')
                passwd = self.recv_packed_bytes()
                if account_list[user_name] != passwd:
                    self.send_packed_bytes('密码错误！')
                else:
                    self.send_packed_bytes('success')
                    self.user_name = user_name.decode('utf8')
                    break

    def create_user_space(self):
        os.chdir(Server.main_path + '/' + self.user_name)

    def deal_command(self):
        while True:
            try:
                command = self.recv_packed_bytes().decode('utf8')
                print(command)
            except:
                break
            if command[:2] == 'ls':
                self.op_ls()
            elif command[:2] == 'cd':
                self.op_cd(command)
            elif command[:2] == 'rm':
                self.op_rm(command)
            elif command[:3] == 'pwd':
                self.op_pwd()
            elif command[:4] == 'gets':
                self.op_gets()
            elif command[:4] == 'puts':
                self.op_puts()

    def op_ls(self):
        file_detail = Server.show_file_detail(os.getcwd())
        self.send_packed_bytes(file_detail)

    def op_cd(self, command):
        # print(command.split()[1])
        try:
            os.chdir(command.split()[1])
        except FileNotFoundError:
            self.send_packed_bytes('没有这个目录')
        except NotADirectoryError:
            self.send_packed_bytes('目录名称无效')
        else:
            self.send_packed_bytes(os.getcwd())

    def op_rm(self, command):
        file_name = command.split()[1]
        try:
            os.remove(file_name)
        except PermissionError:
            try:
                os.rmdir()
            except OSError:
                self.send_packed_bytes('目录不是空的')
        except FileNotFoundError:
            self.send_packed_bytes('文件不存在')
        else:
            self.send_packed_bytes('文件已删除！')

    def op_pwd(self):
        self.send_packed_bytes(os.getcwd())

    def op_gets(self):
        print(self.user_name)
        file_detail = Server.show_file_detail(
            Server.main_path + '/' + self.user_name)
        self.send_packed_bytes(file_detail)
        file_name = self.recv_packed_bytes().decode('utf8')
        self.send_big_file(file_name)

    def op_puts(self):
        self.recv_big_file()
        self.send_packed_bytes('上传成功')


if __name__ == '__main__':
    server = Server()
    while True:
        server.tcp_init()
        server.start()
