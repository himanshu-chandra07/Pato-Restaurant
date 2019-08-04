from django.contrib import admin
from .models import galleryy,chef,food,menuu,pics,photo,lunch,reservation
# Register your models here.
class Postadmin(admin.ModelAdmin):
    list_display=['name','cat','price']

admin.site.register(galleryy)
admin.site.register(chef)
admin.site.register(food)
admin.site.register(menuu,Postadmin)
admin.site.register(photo)
admin.site.register(pics)
admin.site.register(lunch)
admin.site.register(reservation)
