import datetime
from django import forms
from django.db import models
from django.urls import reverse
from django.utils import timezone
from weekfun.settings import AUTH_USER_MODEL


"""
Event 
- Name
- Adresse 
- Lowest_Price
- Highest_Price
- Availibility
- Description 
- Image
"""


class Event(models.Model):
    Name = models.CharField(max_length=120)
    Slug = models.SlugField(max_length=128)
    Adresse = models.CharField(max_length=240)
    Country = models.CharField(max_length=128)
    Date = models.DateField(default=datetime.date(2023, 1, 1))
    Lowest_Price = models.FloatField(default=0.0)
    Highest_Price = models.FloatField(default=0.0)
    Availibility = models.BooleanField(default=True)
    Description = models.TextField(blank=True)
    Image = models.ImageField(upload_to="images/", null=True, blank=True)
    Category = models.CharField(max_length=64)
    Trending = models.BooleanField(default=True)
    Type = models.CharField(max_length=64, default="Public")

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("event", kwargs={"slug": self.Slug})

class Order(models.Model):
    User = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Ordered = models.BooleanField(default=False)
    Ordered_date = models.DateField( blank=True, null=True)

    def __str__(self):
        return f"{self.Event.Name} ({self.Quantity})"

    def delete(self, *args, **kwargs):
        for order in self.User.order_set.all():
          order.Ordered = True
          order.Ordered_date = timezone.now()
          order.save()

        self.User.order_set.set([])
        super().delete(*args, **kwargs)

class Cart(models.Model):
    User = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    Order = models.ManyToManyField(Order)


    def __str__(self):
        return self.User.username
    
    def delete(self, *args , **kwargs):
        for order in self.Order.all():
            order.Ordered = True
            order.Ordered_date = timezone.now() 
            order.save()
        
        self.Order.clear()
        super().delete(*args, **kwargs)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'Name',
            'Slug',
            'Adresse',
            'Country',
            'Date',
            'Lowest_Price',
            'Highest_Price',
            'Availibility',
            'Description',
            'Image',
            'Category',
            'Type',
        )

class PromoCode(models.Model):
    Code = models.CharField(max_length=64)
    Discount = models.FloatField(default=0.0)

    def __str__(self):
        return self.Code