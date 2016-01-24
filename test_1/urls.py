"""test_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin
from firstapp import views

#import api.py in firstapp
from firstapp import api
#User modul
from django.contrib.auth.models import User

#Django-rest framework
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

from firstapp.views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    home,
	androidapp,
    )

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, {}),
	url(r'^androidapp', androidapp, {}),
    url(r'^list', post_list),
    url(r'^create/', post_create),
    url(r'^detail/', post_detail),
    url(r'^update/', post_update),
    url(r'^delete/', post_delete),
	url(r'^api/', include(router.urls)),
	url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/question/$', api.QuestionList.as_view()),
	]


