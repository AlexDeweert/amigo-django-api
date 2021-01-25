from django.urls import path

from amigoapi.views import users

urlpatterns = [
    path('users/', users.get_user, name='user-details'),
    #path('timers/', views.index, name='index'),
    #path('intervals/', views.index, name='index'),
    #path('register/', views.index, name='index'),
    #path('login/', views.index, name='index'),
]
