"""leaveproject URL Configuration

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

from django.contrib import admin
from django.urls import path, include
from leaveappdata import views
from django.conf import settings
from django.conf.urls.static import static
from leaveusers import views as leaveuser_views
from django.contrib.auth import views as authviews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('leaveappdata/', include('leaveappdata.urls')),
    path('register/', leaveuser_views.register, name='register'),
    path('profile/', leaveuser_views.profile, name='profile'),
    path('login/', authviews.LoginView.as_view(template_name='leaveusers/login.html'), name='login'),
    path('logout/', authviews.LogoutView.as_view(template_name='leaveusers/logout.html'), name='logout'),
    path('', views.home, name='home'),
    path('leave_form/', views.leave_form, name='leave_form'),
    path('showdata_approved/', views.showdata_approved, name='showdata_approved')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
