from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
    path('upload/', views.image_upload, name='upload'),
    path('', views.image_list, name='list'),
]