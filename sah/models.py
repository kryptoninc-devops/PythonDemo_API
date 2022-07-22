from django.db import models

# Create your models here.
class Category(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):

        return self.name
    
class Product(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image')
    video = models.FileField(upload_to='videos_uploaded',null=True)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    
    
    

    
    

    
    
   