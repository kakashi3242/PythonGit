# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券）
#            使用 Python 如何生成 200 个激活码（或者优惠券）？//并保存到数据库


from random import Random
import pymysql

# pymysql.install_as_MySQLdb()


def activation_code(codeLength=10):
    code = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(codeLength):
        code+=chars[random.randint(0, length)]
    return code

def insert(code):
        # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "123", "python" )

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # sql = "INSERT INTO ACTION_CODE (action_code) VALUES ('ii')"
    sql = "INSERT INTO ACTION_CODE (action_code) VALUES ('"+code+"')"
    print(sql)
    cursor.execute(sql)

    # 更新数据库

    db.commit()
    # 关闭数据库连接
    db.close()



if __name__ == '__main__':
    for i in range(1,20):
        aCode = activation_code()
        print(aCode)
        insert(aCode)





