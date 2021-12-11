from django.urls import path
from . import views
app_name = "homepage"
urlpatterns = [
    path("", views.index, name="index"),
    path('new/',views.new_project, name = 'new_project'),
]