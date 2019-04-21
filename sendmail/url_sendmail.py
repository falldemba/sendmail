from django.conf.urls import url
import django.contrib.auth.views
import sendmail.views

urlpatterns=[
    url(r'^login$',sendmail.views.login, name='login'),
    url(r'^home$', sendmail.views.home, name='home'),
]
