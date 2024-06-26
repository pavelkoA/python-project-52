"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from task_manager import views
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path('logout/', views.UserLogoutView.as_view(), name='logout'),
    url('logout/', 'django.contrib.auth.views.logout', name='logout'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.IndexView.as_view(), name='task_manager_index'),
    path("", include("django.contrib.auth.urls")),
    path('users/', include('task_manager.users.urls'))
)
