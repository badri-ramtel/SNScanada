from django.contrib import admin
from django.urls import path
from main_app import views

# Django Admin page Customize
admin.site.site_header = "SNS Canada Admin"
admin.site.site_title = "Welcome to SNS Canada Admin page"
admin.site.index_title = "SNS Canada Administration"

urlpatterns = [
    path('', views.home, name='mainapp-home'),
    path('president/', views.president, name='mainapp-president'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('advertise/<str:pk>', views.advertise, name='advertise'),
]