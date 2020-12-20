from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.login,name='login'),
    path('startquiz',views.startquiz,name='startquiz'),
#    path('questions',views.questions,name='questions'),
    path('quizpage',views.quizpage,name='quizpage'),

]
