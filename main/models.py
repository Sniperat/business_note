from django.db import models


class OrderModel(models.Model):
    customer = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()
    prepayment = models.BooleanField(default=False)
    prepayment_quantity = models.IntegerField(default=0)

    STATUS = (
        (0, 'Waiting'),
        (1, 'InProgress'),
        (2, 'Shipping'),
        (3, 'Delivered'),

    )
    status = models.PositiveSmallIntegerField(choices=STATUS, default=0)
    cteated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def total_price(self):
        return sum(self.products.values_list("price", flat=True))
    
    
    def __str__(self) -> str:
        return self.customer
    


class ProductModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='products')
    group = models.ForeignKey('GroupModel', on_delete=models.CASCADE, related_name='products')
    size = models.ForeignKey('SizeModel', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    comment = models.TextField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name

    


class ImageModel(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)


class GroupModel(models.Model):
    
    name = models.CharField(max_length=52)

    def __str__(self) -> str:
        return self.name
    
class SizeModel(models.Model):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='sizes')
    size = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.size
