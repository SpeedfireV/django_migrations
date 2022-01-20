from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):

    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class ProductType(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.color, self.size}"


class Order(models.Model):
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    surname = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.surname} - {self.created}"


class OrderPosition(models.Model):
    product_type = models.ForeignKey("ProductType", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.amount}"


class Payment(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.order} - {self.status}"




