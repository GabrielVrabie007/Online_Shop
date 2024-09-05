from pickle import TRUE
from django.db import models

# Create your models here.


# verbose_name este denumirea la admin panel cand adaugam o noua categorie
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=TRUE, verbose_name="Name")
    slug = models.SlugField(
        max_length=200, blank=True, unique=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Categorie"

    def __str__(self):
        return self.name


class Products(models.Model):

    name = models.CharField(max_length=150, unique=TRUE, verbose_name="Name")
    slug = models.SlugField(
        max_length=200, blank=True, unique=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="image"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Price"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=0, verbose_name="Discount Price"
    )
    quantity = models.PositiveBigIntegerField(default=0, verbose_name="Quantity")

    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Category"
    )

    class Meta:
        db_table = "Product"
        verbose_name = "Product"
        ordering = ("id",)

    def __str__(self):
        return self.name

    def display_id(self):
        return f"{self.id:05}"

    def verify_discount(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
