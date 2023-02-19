from django.urls import path,include
from .views import home,post,category

urlpatterns = [
    path('',home),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category)
]