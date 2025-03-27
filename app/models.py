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

class History(models.Model):
    id = models.AutoField("id",primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = "history"