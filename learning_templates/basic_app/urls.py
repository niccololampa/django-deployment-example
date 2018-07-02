from django.conf.urls import url
from basic_app import views

#template tagging
#set a global variable name called app_name and wet it to whatever the name of your application is.

app_name = 'basic_app'

#$ sign means anything after relative/other
urlpatterns = [    
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
