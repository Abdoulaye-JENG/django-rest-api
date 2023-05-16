from django.db import models
from django.contrib.auth import get_user_model
from products.utils.functions import generate_random_string

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=00.99)

    @property
    def sale_price(self):
        return f"{float(self.price) - float(self.price) * 0.75:.2f}"

    def get_discount(self):
        return f"{float(self.price) * 0.8:.2f}"


class Stock(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=255)
    storing_conditions = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("name", "location"),)


class StorageReceipt(models.Model):
    class StatusChoices(models.TextChoices):
        VALID = "VALID", "VALID"
        INVALID = "INVALID", "INVALID"

    reference_number = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    withdrawal_terms = models.TextField()
    status = models.CharField(
        max_length=10, choices=StatusChoices.choices, default=StatusChoices.VALID
    )
    valid_until = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(StorageReceipt, self).save(*args, **kwargs)
        rdm_str = generate_random_string(length=11)
        rdm_str_first_part = rdm_str[:4]
        rdm_str_last_part = rdm_str[4:]
        self.reference_number = f"{rdm_str_first_part}{self.id}{rdm_str_last_part}"
        super(StorageReceipt, self).save(*args, **kwargs)


class ProductBin(models.Model):
    owner = models.ForeignKey(
        User, related_name="product_bins", on_delete=models.CASCADE
    )
    stock = models.ForeignKey(
        "Stock", related_name="product_bins", on_delete=models.CASCADE
    )
    # storage_receipt = models.ForeignKey(
    #     "StorageReceipt", related_name="product_bins", on_delete=models.CASCADE
    # )
    reference_number = models.CharField(max_length=60, unique=True)
    nature = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    packaging = models.TextField()
    quantity = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(ProductBin, self).save(*args, **kwargs)
        rdm_str = generate_random_string(length=11)
        rdm_str_first_part = rdm_str[:4]
        rdm_str_last_part = rdm_str[4:]
        self.reference_number = f"{rdm_str_first_part}{self.id}{rdm_str_last_part}"
        super(ProductBin, self).save(*args, **kwargs)


class Productbin_Storagereceipt(models.Model):
    product_bin = models.ForeignKey("ProductBin", on_delete=models.CASCADE)
    storage_receipt = models.ForeignKey("StorageReceipt", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("product_bin", "storage_receipt"),)
