from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    tg_id = models.BigIntegerField(null=True, blank=True, unique=True)
    tg_username = models.CharField(max_length=70, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='brand')

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='produc_category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='produc_brand')
    hjm = (
        ('0.5', '0.5'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
    )
    name = models.CharField(max_length=70)
    photo = models.ImageField(upload_to='product')
    price = models.IntegerField()
    count = models.IntegerField()
    hajm = models.CharField(max_length=5, choices=hjm, default='1')

    def __str__(self):
        return self.name


class Shop(models.Model):
    client = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='shop_client', null=True)
    status = models.IntegerField(default=0, null=True)
    total = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ShopItems(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, related_name='shopitem_shop')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='shopitem_product')
    quantity = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Savatcha(models.Model):
    client = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='savatcha_client')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class SavatchaItems(models.Model):
    savatcha = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, related_name='savatchaitem_shop')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='savatchaitem_product')
    quantity = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)

