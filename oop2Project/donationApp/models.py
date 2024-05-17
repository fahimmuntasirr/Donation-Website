from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class user_info(models.Model):
#     recipe_name = models.CharField(max_length=100)


class user_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True, blank=True)
    profile_dp = models.ImageField(upload_to="recipe_image", null=True, blank=True )
    date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100,null=True, blank=True)
    donation_amount = models.IntegerField(null=True, blank=True)
    donation_count = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
class donation_list(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    raised = models.IntegerField(null=True,blank=True)
    donation_number = models.CharField(max_length=100,null=True, blank=True)

class donation_details(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    donation_number = models.CharField(max_length=100,null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)

    

