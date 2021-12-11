from django.db import models

# Create your models here.
class Projects(models.Model):
    """
    Class to create a new project
    """
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    project_image = models.ImageField(upload_to='images')
    project_link = models.URLField(max_length=200)
    #user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    date_created= models.DateField(auto_now_add=True )

    def save_projects(self):
        """
        Class method to save project
        """
        self.user

    def delete_projects(self):
        """
       Class method to delete project(id) 
        """
        self.delete()    


    @classmethod
    def search_projects(cls, name):
        """
        Class method to search for a project
        """
        return cls.objects.filter(title__icontains=name).all()

RATE_CHOICES = [
(1,'1- Trash'),
(2,'2- Horrible'),
(3,'3- Terrible'),
(4,'4- Bad'),
(5,'5- Ok'),
(6,'6- Presentable'),
(7,'7- Good'),
(8,'8- Amazing'),
(9,'9- Perfect'),
(10,'10- Veteran!'),
]