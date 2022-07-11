"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('connect.urls')),
    path('reminder/', include('get_reminders_api.urls')),
    path('groups/', include('get_groups_api.urls')),
    path('cgmeetings/', include('get_cgmeetings_api.urls')),
    path('message/', include('get_messages_api.urls')),
    path('contacts/', include('get_contacts_api.urls')),
    path('interviews/', include('get_cginterviews_api.urls')),
    path('profile/', include('get_caregivermprofile_api.urls')),
    path('cart/', include('get_caregivercart_api.urls')),
    path('analytics/', include('get_analytics_app.urls')),
   
    
]
