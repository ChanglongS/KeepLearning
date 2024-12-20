# 作者: 王道 龙哥
# 2022年03月21日16时15分04秒
from recv_msg import *
from handle_msg import *


def main():
    # 1. 接收数据,往列表中放了0,1,2,3,4
    recv_msg()
    # 2. 测试是否接收完毕
    test_recv_data()
    # 3. 判断如果处理完成，则接收其它数据
    recv_msg_next()
    # 4. 处理数据
    handle_data()
    # 5. 测试是否处理完毕
    test_handle_data()
    # 6. 判断如果处理完成，则接收其它数据
    recv_msg_next()


if __name__ == "__main__":
    main()