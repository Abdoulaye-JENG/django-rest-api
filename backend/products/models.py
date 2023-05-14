from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=15, default=00.99)

    @property
    def sale_price(self):
        return f"{float(self.price) - float(self.price) * 0.75:.2f}"

    def get_discount(self):
        return f"{float(self.price) * 0.8:.2f}"
