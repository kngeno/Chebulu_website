# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos

from django.db import models
from urllib2 import URLError
from autoslug import AutoSlugField
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField

from geopy.geocoders import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError 

def image_upload_folder(instance, filename):
    return "maps_images/%s" % (filename)

choices_animals= (        
    ('Carnivores', 'Carnivores'),
    ('Herbivores', 'Herbivores'),
    ('Omnivores', 'Omnivores'),
    ('Fish', 'Fish'),
    ('Birds', 'Birds'), 
    ('Reptiles', 'Reptiles')
)


#Edit types of farm produce
choices_plants = (        
    ('Indigenous', (
            ('Trees', 'Trees'),
            ('Shrubs', 'Shrubs'),
            ('Flowers', 'Flowers'),            
        )
    ),
    ('Foreign',(
            ('Trees', 'Trees'),
            ('Shrubs', 'Shrubs'),
            ('Flowers', 'Flowers'),     
        )
    ),    
)

choices_trails = (
   
    ('Bike_trails', 'Bike_trails'),
    ('Hiking', 'Hiking'),
    ('All_trails', 'All_trails'),
    ('Roads', 'Roads')
)

choices_kaplelartet_places = (        
    
    ('Shops', 'Shops'),
    ('Fuel_stations', 'Fuel_stations'),
    ('Supermarket', 'Supermarket')    
)

choices_chebulu_places = (        
    ('Visitors_Lounge', 'Visitors_Lounge'),
    ('Reptile_Park', 'Reptile_Park'),
    ('Birds_Paradise', 'Birds_Paradise'),
    ('Carnivore', 'Carnivore'),
    ('Fish_Park', 'Fish_Park'),
    ('Monkey_Paradise', 'Monkey_Paradise'),
    ('Hotels', 'Hotels'),
    ('Shops', 'Shops'),
    ('Camps', 'Camps'),
    ('Restaurants', 'Restaurants'),
)

class Animal(models.Model):
    name = models.CharField(" Full Names",max_length=200, unique=True)
    scientific_name = models.CharField(" Scientific Names",max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True) 
    type = models.IntegerField("type",max_length=200,choices=choices_animals)    
    population = models.IntegerField("population", max_length= 50)
    description =models.TextField("Description")
    link = models.URLField("Link", max_length= 200)
    location = gis_models.MultiPointField(u"longitude/latitude", geography=True, blank=True, srid=4326, null=True)
    image = ThumbnailerImageField(upload_to=image_upload_folder, height_field=None, width_field=None, blank=True)
    

    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __unicode__(self):
        return '%s %s' % (self.name, self.location)   

    class Meta:
        ordering = ('name', 'scientific_name', 'type','population','location','image', )
        verbose_name_plural =  ('Animals')


class Trail(models.Model):
    name = models.CharField("Full Names",max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    type = models.CharField("type", max_length=100,choices=choices_trails, default= "Mixed")
    distance = models.FloatField("distance", max_length= 250, default= "None") 
    activity = models.CharField("Dairy", max_length= 250, default= "None")    
    description =models.TextField("Description") 
    link = models.URLField("Link", max_length= 200)
    location = gis_models.MultiLineStringField(u"longitude/latitude", geography=True, blank=True, srid=4326, null=True)    
    image = ThumbnailerImageField(upload_to=image_upload_folder, height_field=None, width_field=None, blank=True)

    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __unicode__(self):
        return '%s %s %s %s ' % (self.name, self.type, self.distance, self.activity)

    class Meta:
        ordering = ('name', 'distance', 'type', 'location','image',)
        verbose_name_plural = ("Trails")       


class Plant(models.Model):
    name = models.CharField("Full Names",max_length=200, unique=True)
    scientific_name = models.CharField("Scientific Names",max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    type = models.CharField("type", max_length=100,choices=choices_plants, default= None)
    description =models.TextField("Description")     
    link = models.URLField("Link", max_length= 200)
    location = gis_models.MultiPointField(u"longitude/latitude", geography=True, blank=True, srid=4326, null=True)
    image = ThumbnailerImageField(upload_to=image_upload_folder, height_field=None, width_field=None, blank=True)
   
    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __unicode__(self):
        return '%s %s' % (self.name, self.location)   

    class Meta:
        ordering = ('name', 'scientific_name', 'type', 'location','image', )
        verbose_name_plural =  ('Plants')

class Kaplelartet_place(models.Model):
    name = models.CharField("Full Names",max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    type = models.CharField("type", max_length=100,choices=choices_kaplelartet_places, default= None)
    use = models.CharField("use",max_length=200, unique=True)
    description =models.TextField("Description")    
    link = models.URLField("Link", max_length= 200)
    location = gis_models.MultiPointField(u"longitude/latitude", geography=True, blank=True, srid=4326, null=True)
    image = ThumbnailerImageField(upload_to=image_upload_folder, height_field=None, width_field=None, blank=True)    

    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __unicode__(self):
        return '%s %s' % (self.name, self.location)    

    class Meta:
        ordering = ('name', 'use', 'type', 'location','image', )
        verbose_name_plural =  ('Kaplelartet_places')


   
class Chebulu_place(models.Model):
    name = models.CharField("Full Names",max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    type = models.CharField("type", max_length=100,choices=choices_chebulu_places, default= None)
    use = models.CharField("use",max_length=200, unique=True)
    description =models.TextField("Description")      
    location = gis_models.MultiPointField(u"longitude/latitude", geography=True, blank=True, srid=4326, null=True)
    image = ThumbnailerImageField(upload_to=image_upload_folder, height_field=None, width_field=None, blank=True)
   
    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __unicode__(self):
        return '%s %s' % (self.name, self.location)

    class Meta:
        ordering = ('name', 'use', 'type', 'location','image', )
        verbose_name_plural =  ('Chebulu_places')
