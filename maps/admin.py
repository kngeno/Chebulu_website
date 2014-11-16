from django.contrib import admin
from farm.models import Animal, Plant, Trail, Kaplelartet_place, Chebulu_place
from django.contrib.gis import admin as geoadmin

class AnimalAdmin(geoadmin.OSMGeoAdmin):

    list_display = ('name', 'scientific_name', 'type','population','location','image', )
    search_fields = ['name', 'scientific_name', 'type', 'location',]
    #search_fields = ('produce',)
    default_lon =  4113018.76068 #36.9654#
    default_lat =  -46755.87145  #-0.4030
    default_zoom = 14
    map_info = True
    map_width = 800
    map_height = 500
   
class TrailAdmin(geoadmin.OSMGeoAdmin):

    list_display = ('name', 'distance', 'type','population','location','image',)
    search_fields = ['name', 'distance', 'type', 'population','location',]
    search_fields = ('produce',)
    default_lon =  4113018.76068 #36.9654#
    default_lat =  -46755.87145  #-0.4030
    default_zoom = 14
    map_info = True
    map_width = 800
    map_height = 500

class PlantAdmin(geoadmin.OSMGeoAdmin):

    list_display = ('name', 'scientific_name', 'type', 'location','image', )
    search_fields = ['name', 'scientific_name', 'type', 'location',]
    search_fields = ('order',)
    default_lon =  4113018.76068 #36.9654#
    default_lat =  -46755.87145  #-0.4030
    default_zoom = 14
    map_info = True
    map_width = 800
    map_height = 500

class Kaplelartet_placeAdmin(geoadmin.OSMGeoAdmin):

    list_display = ('name', 'use', 'type','population','location','image', )
    search_fields = ['name', 'use', 'type','population','location',]
    search_fields = ('produce',)
    default_lon =  4113018.76068 #36.9654#
    default_lat =  -46755.87145  #-0.4030
    default_zoom = 14
    map_info = True
    map_width = 800
    map_height = 500

class Chebulu_placeAdmin(geoadmin.OSMGeoAdmin):

    list_display = ('name', 'use', 'type','population','location','image', )
    search_fields = ['name', 'use', 'type','population','location',]
    search_fields = ('order',)
    default_lon =  4113018.76068 #36.9654#
    default_lat =  -46755.87145  #-0.4030
    default_zoom = 14
    map_info = True
    map_width = 800
    map_height = 500

# Register your models here.
geoadmin.site.register(Farmer, FarmerAdmin)
geoadmin.site.register(Produce, ProduceAdmin)
geoadmin.site.register(Clients, ClientsAdmin)