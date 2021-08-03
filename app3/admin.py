from django.contrib.admin.sites import AdminSite
from app3.models import blog, feedback, page
from django.contrib import admin
from app3.models import blog,page,feedback

# Register your models here.
admin.site.register(blog)
admin.site.register(page)
admin.site.register(feedback)

