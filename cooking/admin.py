from django.contrib import admin
from cooking.models import *

# Register your models here.
class ClientUsersAdmin(admin.ModelAdmin):
    list_display=('First_Name','Last_Name','Number','Email','Password')
admin.site.register(clientUser,ClientUsersAdmin)

# class itemListAdmin(admin.ModelAdmin):
#     list_display=('id','Category_name')
admin.site.register(ItemList)

class itemadmin(admin.ModelAdmin):
    list_display=('Item_Name','Item_price','Item_details','Item_catogary')
admin.site.register(FoodItem,itemadmin)

class bookadmin(admin.ModelAdmin):
    list_display=('Name','Phone_number','Email','Total_person','Booking_date')
admin.site.register(BookTable,bookadmin)

class aboutAdmin(admin.ModelAdmin):
    list_display=('title','Details','Image')
admin.site.register(aboutTable,aboutAdmin)