from django.db import models
from django.utils.html import format_html

# Category models ---------

class Category(models.Model):
    catId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    addDate = models.DateTimeField(auto_now_add=True,null=True)

    def imageTag(self):
        return format_html('<img src="/media/{}" style="width:50px; heigth:50px; border-radius:50%;">'.format(self.image))

    def __str__(self):
        return self.title

# post model ----

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='post/')

    class Media:
        js = ('js/script.js',)

    def __str__(self):
        return self.title