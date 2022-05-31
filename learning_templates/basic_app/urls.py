from django.conf.urls import url
from basic_app import views
from django.urls import path

# for template tagging
app_name = 'basic_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('base/', views.base, name='base')
]
