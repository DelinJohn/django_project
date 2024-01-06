from django.urls import path
from .views import login_user, home, logout_user
urlpatterns = [
    path('', login_user, name='login'),
    path('login/',login_user,name='login'),
    path('home/',home, name='home'),
    path('logout/',logout_user, name='logout'),
]

