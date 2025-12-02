from django.urls import path 
from . import views

app_name = 'planets'

urlpatterns = [
    path("add/", views.planets_add_view, name="planets_add_view"),
    path("all/planets", views.planets_list_view, name="planets_list"),
    path("datail/planet/<int:planet_id>/", views.planet_detail_view, name="planet_detail"),



    
]