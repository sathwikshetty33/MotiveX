from tkinter.font import names

from django.urls import path,include

from . import views

urlpatterns = [
    path('api/', views.api.as_view(),name='api'),
    path('api-info', views.apiinfo,name='apiinfo'),
    path('', views.register, name='reg'),
    path('login/', views.login_view, name='login'),
    path('home/',views.home,name='home'),
    path('delete/',views.dele, name='delete'),
    path('logout/', views.log,name='logout')
]