from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField("id",primary_key=True)
    username = models.CharField("用户名",max_length=255, default='')
    password = models.CharField("密码",max_length=255,default='')
    sex = models.CharField("性别",max_length=255,default='')
    address = models.CharField("地址",max_length=255,default='')
    avatar = models.CharField("头像",max_length=255,default='avatar/default.jpg')
    textarea = models.TextField("个性签名",max_length=255,default='这个人很懒，什么都没有留下')
    creatname = models.DateField("创建时间", auto_now_add=True)

    class Meta:
        db_table = "user"


class Sales(models.Model):
    customer_id = models.CharField("顾客ID", max_length=255, primary_key=True)
    age = models.IntegerField("年龄")
    gender = models.CharField("性别", max_length=50)
    city = models.CharField("城市", max_length=255)
    category = models.CharField("类别", max_length=255)
    product_name = models.CharField("产品名称", max_length=255)
    purchase_date = models.DateField("购买日期")
    purchase_amount = models.DecimalField("购买金额", max_digits=10, decimal_places=2)
    payment_method = models.CharField("支付方式", max_length=255)
    discount_applied = models.BooleanField("是否使用折扣")
    rating = models.IntegerField("评分")
    repeat_customer = models.BooleanField("是否回头客")

    class Meta:
        verbose_name = "销售"
        verbose_name_plural = "销售"
        db_table = "sales"