from django.db import models

# Create your models here.
class clientUser(models.Model):
    First_Name = models.CharField()
    Last_Name  = models.CharField()
    Number = models.CharField()
    Email = models.EmailField()
    Password = models.CharField() 
    
    
class ItemList(models.Model):
    Category_name = models.CharField()
    
    def __str__(self):
        return self.Category_name
    
    
        
class FoodItem(models.Model):
    Item_Name = models.CharField()
    Item_details = models.TextField()
    Item_price = models.IntegerField()
    Item_catogary = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    # Item_img = models.CharField()
    Image = models.ImageField(upload_to='media/items/')
    
class BookTable(models.Model):
    Name = models.CharField()
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

class aboutTable(models.Model):
    Image = models.ImageField(upload_to='media/about/')
    title = models.CharField()
    Details = models.TextField()