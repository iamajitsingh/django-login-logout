"""Login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Login/urls.py
from django.contrib import admin
from django.urls import path, include  # Added include module
from django.conf import settings
from django.conf.urls.static import static

from passwordGenerator import views

urlpatterns = [

    # Password Generator URLs
    path('choosepassword', views.passhome, name='passhome'),
    path('generatedpassword/', views.password, name='password'),

    path('admin/', admin.site.urls), # Django-Admin
    path('', include('account.urls')),  # Added account app
    path('userprofile/', include('userprofile.urls'), name='userprofile'),  # Added user profile app

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
