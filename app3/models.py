from django.db import models
# from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    # content = RichTextField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True,blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + '|' + str(self.author)
    
class page(models.Model):
    STATUS =(
        ('True', 'True'),
        ('false', 'false')
    )
    slug = models.SlugField(max_length=200, unique=True)
    number = models.IntegerField()
    Question =  models.CharField(max_length=200) 
    Answer =  models.CharField(max_length=500)
    status = models.CharField(max_length=10,choices=STATUS)
   
    def __str__(self):
        return self.Question

class feedback(models.Model):
    image = models.ImageField(null=True,blank=True)
    description = models.TextField(default="") 

