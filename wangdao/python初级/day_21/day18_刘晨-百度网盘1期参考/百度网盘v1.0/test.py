# create by liuchen 2022/3/5 15:40
import os
import dbm

# print('ls1234'[:3])
# print(os.listdir())
file = dbm.open('account', 'c')
# file['liuchen'] = '123'
# print(os.listdir('liuchen'))
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# fd = open('11.txt', 'w')
# fd.write('12345')
# fd.write('111111111')
# os.rmdir('local')
# print(os.stat('local'))
# os.remove('loca')
print(file.keys())
print(file.values())
file.pop(b'lc')
file.pop(b'liiuchen')
print(file.keys())
# os.mkdir('lc')