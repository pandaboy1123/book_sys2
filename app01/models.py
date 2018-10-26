from django.db import models

# Create your models here.


#作者详情表
class AuthorDeatil(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


# 出版社表
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()


# 书籍表
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.ForeignKey(to="Publish", to_field="nid", on_delete=models.CASCADE)
    # 多对多关系表
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title


# 作者表
class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    authordetail = models.OneToOneField(to="AuthorDeatil", to_field="nid", on_delete=models.CASCADE)

    def __str__(self):
        return self.name