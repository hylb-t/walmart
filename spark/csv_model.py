import os
import django

# 设置DJANGO_SETTINGS_MODULE环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'walmart.settings')
django.setup()

from app.models import Sales

# 导入CSV数据并添加到Sales模型
import csv

csv_file_path = './cleaned_Walmart_customer_purchases.csv'

with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Sales.objects.create(
            customer_id=row['Customer_ID'],
            age=row['Age'],
            gender=row['Gender'],
            city=row['City'],
            category=row['Category'],
            product_name=row['Product_Name'],
            purchase_date=row['Purchase_Date'],
            purchase_amount=row['Purchase_Amount'],
            payment_method=row['Payment_Method'],
            discount_applied=row['Discount_Applied'] == 'Yes',
            rating=row['Rating'],
            repeat_customer=row['Repeat_Customer'] == 'Yes'
        )