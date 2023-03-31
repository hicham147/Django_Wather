from django.urls import path
from .views import index
namespace='watherApp'
urlpatterns = [
    path('',index,name='index'),]
