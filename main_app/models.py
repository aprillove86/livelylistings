from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User 



RANGES = (
    ('low', 'Affordable'),
    ('medium', 'Wish List'),
    ('high', 'Over Budget'),
)


class Listing(models.Model):

    community = models.CharField(max_length=65) ###name of the apt community
    neighborhood = models.CharField(max_length=25) 
    price = models.IntegerField()
    beds = models.IntegerField()
    baths = models.DecimalField(max_digits=2, decimal_places=1)
    sqft = models.IntegerField()   
    main_photo = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.community

    def get_absolute_url(self):
        return reverse("listings_detail", kwargs={'pk': self.id})

    class Meta:
        ordering = ('-price', 'neighborhood')


class Liveable(models.Model):
    
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE) ###will be able to choose a favorite neighborhood
    description = models. CharField(max_length=300)
    listings = models.ManyToManyField(Listing)
    photo = models.ImageField(upload_to='photos/', blank=True)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"liveable_id": self.id})
  

class Affordability(models.Model):
    
    budget = models.CharField(max_length=20, choices=RANGES, default=RANGES[0][0])
    liveable = models.ForeignKey(Liveable, on_delete=models.CASCADE)

    def __str__(self):
        return self.budget

    class Meta:
        ordering = ('budget',)



