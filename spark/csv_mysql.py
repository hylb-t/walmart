import pandas as pd
import pymysql
from sqlalchemy import create_engine

# 1. 读取 CSV 数据
csv_file = '/mnt/data/cleaned_Walmart_customer_purchases.csv'
df = pd.read_csv(csv_file)
print("CSV 文件预览:")
print(df.head())
print("字段及数据类型:")
print(df.dtypes)

# 2. 根据数据类型映射 MySQL 类型
def map_dtype(dtype):
    if 'int' in str(dtype):
        return "INT"
    elif 'float' in str(dtype):
        return "DECIMAL(10,2)"
    elif 'datetime' in str(dtype):
        return "DATETIME"
    else:
        return "VARCHAR(255)"

# 生成每个字段的建表语句部分
columns = df.columns
sql_columns = []
for col in columns:
    col_type = map_dtype(df[col].dtype)
    sql_columns.append(f"`{col}` {col_type}")

# 注意：此处额外增加了自增主键 id
sql_columns_sql = ",\n  ".join(sql_columns)
create_table_query = f"""
CREATE TABLE IF NOT EXISTS customer_purchases (
  id INT AUTO_INCREMENT PRIMARY KEY,
  {sql_columns_sql}
);
"""
print("生成的建表语句:")
print(create_table_query)

# 3. 连接 MySQL 创建数据库和表
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='000000',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
try:
    with conn.cursor() as cursor:
        # 创建数据库
        cursor.execute("CREATE DATABASE IF NOT EXISTS walmart_db;")
        cursor.execute("USE walmart_db;")
        # 创建表
        cursor.execute(create_table_query)
    conn.commit()
finally:
    conn.close()

# 4. 利用 SQLAlchemy 将数据导入 MySQL 表
engine = create_engine('mysql+pymysql://root:000000@localhost/walmart_db')
df.to_sql('customer_purchases', con=engine, if_exists='append', index=False)

print("数据已成功导入 MySQL 数据库！")
