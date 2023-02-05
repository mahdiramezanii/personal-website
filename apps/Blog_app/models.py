from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
class Tag(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.name

class Article(models.Model):
    auther=models.CharField(max_length=50,default="مهدی رمضانی")
    titel=models.CharField(max_length=200)
    tag=models.ManyToManyField(Tag,related_name="Article")
    image=models.ImageField(upload_to="media/mag/image")
    created=models.CharField(max_length=50)
    slug=models.SlugField()
    body=RichTextField()


    def get_absolut_url(self):

        return reverse("Blog_app:Blog-post",kwargs={"slug":self.slug})


    def __str__(self):

        return self.titel