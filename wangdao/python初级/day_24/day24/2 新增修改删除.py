# 作者: 王道 龙哥
# 2022年03月12日11时21分56秒
from pymysql import *

def main():
    # 创建Connection连接
    conn = connect(host='192.168.19.130',port=3306,database='python5',
                   user='root',password='123',charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行insert语句，并返回受影响的行数：添加一条数据
    # 增加
    # count = cs1.execute('insert into goods_cates(name) values("硬盘")')
    # #打印受影响的行数
    # print(count)
    #
    # count = cs1.execute('insert into goods_cates(name) values("光盘")')
    # print(count)

    # # 更新
    # count = cs1.execute('update goods_cates set name="机械硬盘" where name="硬盘"')
    # print(count)
    # # 删除
    count = cs1.execute('delete from goods_cates where id>10')
    print(count)
    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交，忘记commit数据库没改变
    conn.commit()

    # 关闭Cursor对象
    cs1.close()
    # 关闭Connection对象
    conn.close()

if __name__ == '__main__':
    main()