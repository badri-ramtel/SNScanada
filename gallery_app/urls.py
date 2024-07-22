from django.urls import path
from gallery_app import views

urlpatterns = [
    path('', views.gallery, name='galleryapp-gallery'),
    path('gridview/<str:pk>', views.gridView, name='galleryapp-gridview'),
    path('grid/<str:grid_id>/photo/<str:pk>', views.viewPhoto, name='galleryapp-photo'),
]