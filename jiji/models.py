#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
STATE = (
        ("Abia","Abia"),
        ("Adamawa","Adamawa"),
        ("Akwa Ibom","Akwa Ibom"),
        ("Anambra","Anambra"),
        ("Bauchi","Bauchi"),
        ("Bayelsa","Bayelsa"),
        ("Benue","Benue"),
        ("Borno","Cross River"),
        ("Cross River","Cross River"),
        ("Delata","Delta"),
        ("Ebonyi","Ebonyi"),
        ("Edo","Edo"),
        ("Ekiti","Ekiti"),
        ("Enugu","Enugu"),
        ("Gombe","Gombe"),
        ("Imo","Imo"),
        ("Jigawa","Jigawa"),
        ("Kaduna","Kano"),
        ("Katsina","Katsina"),
        ("Kebbi","Kebbi"),
        ("Kogi","Kogi"),
        ("Kwara","Kwara"),
        ("Lagos","Lagos"),
        ("Nasarawa","Nasarawa"),
        ("Niger","Niger"),
        ("Ogun","Ogun"),
        ("Ondo","Ondo"),
        ("Osun","Osun"),
        ("Oyo","Oyo"),
        ("Plateau","Plateau"),
        ("Rivers","Rivers"),
        ("Sokoto","Taraba"),
        ("Yobe",'Yobe'),
        ("Zamfara","Zamfara"),
        )
        
class User(AbstractUser):
    state_of_residence = models.CharField(max_length=25,choices=STATE)
    
class Product(models.Model):
    seller= models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    description = models.TextField()
    #location = models.CharField(max_length=250,default="")
    #buyer =models.ForeignKey(Interests)
    image =models.ImageField(upload_to='Images/', default='profile_pics/default.jpg')
    is_sold = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='Products'
        ordering =('-created',)
    
    
    def __str__(self):
        return self.name
        

class Interests(models.Model):
    name =models.CharField(max_length=50)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='interests',default='')
    email = models.EmailField()
    location = models.CharField(max_length=250,default="")
    created =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('created',)

    def __str__(self):
        return f'interest shown by {self.name} on {self.product} with email: {self.email}'
