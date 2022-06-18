from django.db import models

# Clase: registra en la BD las categorias en la página.
class Category(models.Model):
    name = models.CharField(max_length=20)
#    image = models.ImageField(upload_to = "Category Images", null=True, blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


# Clase: registra en la BD los productos en la página.
class Products(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField()
    inStock = models.BooleanField(default=False)
#    image = models.ImageField(upload_to = "Produc Images", null=True)
#    image2 = models.ImageField(upload_to = "Produc Images", null=True, blank=True)
#    image3 = models.ImageField(upload_to = "Produc Images", null=True, blank=True)
#    image4 = models.ImageField(upload_to = "Produc Images", null=True, blank=True)
#    image5 = models.ImageField(upload_to = "Produc Images", null=True, blank=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ('-price',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.quantity == 0:
            self.inStock = False
        else:
            self.inStock = True
        super().save(*args, **kwargs)