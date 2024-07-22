from django.urls import path
from about_app import views

urlpatterns = [
    path('abouts/', views.aboutUs, name='aboutapp-about'),
    path('vision/', views.vision, name='aboutapp-vision'),
    path('terms/', views.terms, name='aboutapp-terms'),
    path('news/', views.news, name='aboutapp-news'),
    path('news/viewnews/<str:pk>', views.viewNews, name= 'aboutapp-viewnews'),
]