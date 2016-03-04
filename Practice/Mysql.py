import pymysql

def insert(user_name, user_password):
        # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "123", "python" )

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 插入固定字符
    # sql = "insert into USER (user_name, user_password) VALUES ('ww','111111')"
    # sql = "INSERT INTO ACTION_CODE (action_code) VALUES ('ii')"
    # 插入变量
    # sql = "INSERT INTO ACTION_CODE (action_code) VALUES ('"+code+"')"
    # 选择指定字段
    sql = "select user_password from USER WHERE user_name = '"+user_name+"'"
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchone()
    if user_password in result:
        print('done')
    else:
        print('WRONG PASSWORD')

    db.commit()
    # 关闭数据库连接
    db.close()
    return result

if __name__ == '__main__':
    code = 'wy'
    password = '111111'
    print( insert(code, password))