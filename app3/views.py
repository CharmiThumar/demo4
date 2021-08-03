from typing import ContextManager
from django.db.models.query import QuerySet
from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.list import ListView
from.models import blog, feedback
from.form import blog,page,feedback
from app3 import form

class show(generic.ListView):
    queryset = blog.objects.filter(status=1).order_by('-created_on')
    queryset = page.objects.filter(status=True).order_by("number")
    queryset = feedback.objects.all()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['post_list1'] = blog.objects.all()
        context ['post_list'] = page.objects.order_by("number")
        context ['post_list2'] = feedback.objects.all()
        return context   

