"""localOlx URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home','home.views.index',name="home"),
    url(r'^login','home.views.login',name="login"),
    url(r'^signup','home.views.signup',name="signup"),
    url(r'^additem','home.views.additem',name="additem"),
    url(r'^logout','home.views.logout',name="logout"),
    url(r'^myitem','home.views.myitem',name="myitem"),
    url(r'^help','home.views.help',name="help"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
