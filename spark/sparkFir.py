import pandas as pd
from sqlalchemy import create_engine
import pymysql

# 数据库配置信息
user = 'root'
password = '000000'
host = 'localhost'
database = 'walmart_db'           # 数据库名称，可自行修改
table_name = 'cleaned_Walmart_customer_purchases'  # 表名
csv_file = './cleaned_Walmart_customer_purchases.csv'  # CSV 文件路径

# 1. 读取 CSV 文件
df = pd.read_csv(csv_file)
print("CSV 数据加载成功，数据维度：", df.shape)

# 2. 根据 DataFrame 各字段的数据类型生成对应的 MySQL 列定义
def generate_create_table_sql(df, table_name):
    col_defs = []
    for col in df.columns:
        dt = df[col].dtype
        # 判断整数类型
        if pd.api.types.is_integer_dtype(dt):
            col_type = 'INT'
        # 判断浮点类型
        elif pd.api.types.is_float_dtype(dt):
            col_type = 'FLOAT'
        # 判断布尔类型
        elif pd.api.types.is_bool_dtype(dt):
            col_type = 'TINYINT(1)'
        # 判断日期或时间类型
        elif pd.api.types.is_datetime64_any_dtype(dt):
            col_type = 'DATETIME'
        # 默认使用字符串类型，根据实际字符串长度设置 VARCHAR 长度
        else:
            # 获取该列最大字符串长度
            max_len = df[col].astype(str).map(len).max()
            if pd.isna(max_len) or max_len < 1:
                max_len = 50
            # 为避免过长，可以设置上限，比如 500
            max_len = min(max_len, 500)
            col_type = f'VARCHAR({max_len})'
        col_defs.append(f"`{col}` {col_type}")
    col_defs_str = ",\n  ".join(col_defs)
    sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` (\n  {col_defs_str}\n);"
    return sql

create_table_sql = generate_create_table_sql(df, table_name)
print("生成的建表 SQL：")
print(create_table_sql)

# 3. 创建数据库（如果不存在）
# 先连接到 MySQL（不指定数据库）
conn = pymysql.connect(host=host, user=user, password=password)
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
conn.commit()
cursor.close()
conn.close()
print(f"数据库 {database} 已创建（如果之前不存在）。")

# 4. 创建数据库连接（使用 SQLAlchemy）
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# 5. 通过 pymysql 执行建表语句（如果表不存在则创建）
conn = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
cursor.execute(create_table_sql)
conn.commit()
cursor.close()
conn.close()
print(f"数据表 {table_name} 已创建（如果之前不存在）。")

# 6. 将数据写入 MySQL 表中，采用 append 模式（假设表结构与 CSV 字段一致）
df.to_sql(name=table_name, con=engine, if_exists='append', index=False, method='multi')
print(f"数据已成功写入数据库 {database} 中的表 {table_name}.")
