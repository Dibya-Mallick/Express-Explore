from django.forms import ModelForm
from .models import Blogs

class BlogsForm(ModelForm):
    class Meta:
        model=Blogs
        fields=['title','body']