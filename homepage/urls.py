from django.urls import path,include
from . import views
app_name = "homepage"
urlpatterns = [
    path("", views.index, name="index"),
    path('new/',views.new_project, name = 'new_project'),
    path('projects/<id>/',views.projects, name = 'projects'),
    
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
]