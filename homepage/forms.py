from django import forms
from .models import Projects
class ProjectForm(forms.ModelForm):
    """
    Form class to create an html form from the projects model
    """
    class Meta:
        model = Projects
        fields = ['title','description','project_image','project_link']