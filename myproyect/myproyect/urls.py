"""myproyect URL Configuration

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
from django.conf.urls import url , patterns , include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/profile/$', 'cms_templates.views.inicio'),
    url(r'^pages$', 'cms_templates.views.mostrar'),
    url(r'^annotated/(\d+)$', 'cms_templates.views.annotated_identificador'),
    url(r'^annotated/(.*)$', 'cms_templates.views.annotated_recurso'),
    url(r'^(\d+)$', 'cms_templates.views.identificador'),
    url(r'^(.*)$', 'cms_templates.views.recurso')
]
