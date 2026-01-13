from django.db import models

class categoryModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
class productModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True)
    category=models.ForeignKey(categoryModel, on_delete=models.CASCADE, null=True, related_name='cat_name')
    image=models.ImageField(max_length=100, upload_to='Media/productImage', null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock_quantity=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name