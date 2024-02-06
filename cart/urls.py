"""
URL configuration for shopping project.

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
from django.urls import path
from . import views
from django.conf import settings
from .views import cart
from django.conf.urls.static import static
from .views import delete_from_cart


# from django.conf.urls.settings import static

urlpatterns = [

    path('login', views.login_view, name='login'),
    path('logout', views.user_logout ,name='logout'),
    path('bucket', views.bucket ,name='bucket'),
    path('search', views.search, name='search'),
    path('registration', views.user_registration, name='registration'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('show/', views.cart, name='show'),
    path('delete_from_cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

