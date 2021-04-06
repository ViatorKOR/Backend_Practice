from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog_post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    content = RichTextUploadingField()
   
    