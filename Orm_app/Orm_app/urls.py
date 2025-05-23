"""
URL configuration for Orm_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from orm import views
from rest_framework.authtoken.views import obtain_auth_token  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('orm.urls')),
    path('', views.index, name='home'),
    path('api/create/', views.ItemCreateView.as_view(), name='create-post'),
    path('api/get-all-items/', views.ItemListView.as_view(), name='get-items'),
    path('api/get-item/<int:pk>/', views.GetUserView.as_view(), name='get-user'),
    path('api/update/<int:pk>/', views.UpdateUserView.as_view(), name='update-user'),
    path('api/delete/<int:pk>/', views.DeleteUserView.as_view(), name='delete-user'),
    path('api/posts/<int:pk>/', views.ItemRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('api/login/', obtain_auth_token, name='custom-login'),
]
