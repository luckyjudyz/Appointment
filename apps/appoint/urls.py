from django.conf.urls import url
from . import views

app_name='appoint'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^appointments$', views.appointments, name="appointments"),
    url(r'^edit/(?P<id>)\d+$', views.edit, name="edit"),
	url(r'^register$', views.log_register, name="register"),
	url(r'^login$', views.log_register, name="login"),
	url(r'^logout$', views.logout, name="logout"),
    url(r'^addappoint$', views.addappoint, name="addappoint"),
    url(r'^delete/(?P<id>)\d+/$', views.delete, name="delete"),
]
'appoint:index'
'appoint:appointments'
'appoint:delete'
