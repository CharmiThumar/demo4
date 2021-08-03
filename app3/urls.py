from django.urls import path
from.import views 

urlpatterns = [
    path('blog/', views.show.as_view(), name='index'),

]