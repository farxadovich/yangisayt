from django.urls import path

from  . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('second/', views.second),
    path('uch/', views.uch, name='uch'),
    path('tort/', views.tort, name='tort'),
    path('besh/', views.besh, name='besh'),
    path('olti/', views.olti, name='olti'),
    path('yetti/', views.yetti, name='tetti'),
    path('sakkiz/', views.sakkiz, name='sakkiz'),
    path('toqqiz/', views.toqqiz, name='toqqiz'),
    path('on/', views.on, name='on'),

]