
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"   


urlpatterns = [
    path('profile/<id>/',views.profile,name = 'profile'),
    #path('profile/',views.user_profile,name = 'user_profile'),
    path('edit_profile/',views.edit_profile,name = 'edit_profile'), 
    path("/", views.register, name="register"),

    

]