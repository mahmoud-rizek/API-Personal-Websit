from django.db import models
from django.utils.translation import gettext as _
from django_countries.fields import CountryField
from django.utils import timezone
from birthday import BirthdayField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class info(models.Model):
    fName = models.CharField(_("Frist Name"), max_length=50)
    sName = models.CharField(_("Last Name"), max_length=50)
    education = models.CharField(_("Education"), max_length=80)
    country = CountryField()
    birthDay = BirthdayField()
    phoneNumber = PhoneNumberField(blank=True, region="EG")

    def __str__(self):
        return self.fName
    

class post(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    content = models.TextField(_("Content"), max_length=1000)
    date = models.DateTimeField(_("Post Date"), default=timezone.now())
    comment = 'relation'
    
    def __str__(self):
        return self.title

    

class comment(models.Model):
    content = models.TextField(_("Comment"), max_length=1000)
    date = models.DateTimeField(_("Comment Date"), default=timezone.now())
    
    def __str__(self):
        return str(self.date)
    

    

class project(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    github_Url = models.URLField(_("Github Url"), max_length=200)
    about = models.TextField(_("about"), max_length=1000)
    fetures = models.TextField(_("fetures"), max_length=1000)
    techUses = models.CharField(_("Technologies Used"), max_length=500)
    date = models.DateTimeField(_("Project Date"), default=timezone.now())
    def __str__(self):
        return self.name
    