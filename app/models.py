from django.db import models

# Create your models here.
class galleryy(models.Model):
        img=models.ImageField(blank=True,null=True)
        title=models.CharField(max_length=160)

        def __str__(self):
            return self.title

class chef(models.Model):
        name=models.CharField(max_length=160)
        designation=models.CharField(max_length=140)
        pic=models.ImageField(blank=True,null=True)
        about=models.TextField()

        def __str__(self):
            return self.name
class food(models.Model):
    name=models.CharField(max_length=160)
    def __str__(self):
            return self.name

class menuu(models.Model):
    cat=models.ForeignKey(food,on_delete=False)
    name=models.CharField(max_length=160)
    info=models.CharField(max_length=180)
    price=models.FloatField()
    def __str__(self):
            return self.name

class lunch(models.Model):
    name=models.CharField(max_length=190)
    info=models.CharField(max_length=250)
    price=models.FloatField()
    img=models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.name

class photo(models.Model):
        type=models.CharField(max_length=180)
        def __str__(self):
            return self.type

class pics(models.Model):
    cat=models.ForeignKey(photo,on_delete=False)
    img=models.ImageField(blank=True,null=True)
    def __str__(self):
            return self.cat

class reservation(models.Model):
    nameq=models.CharField(max_length=200,null=True)
    phoneq=models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=150,null=True)
    email=models.EmailField(null=True)
    time=models.CharField(max_length=100,null=True)
    people=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.nameq
