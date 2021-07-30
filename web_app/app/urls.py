from django.urls import path
from .views import *
urlpatterns = [
    # path('<int:id>', new_by_id, name='new_by_id'),
    path('dsdc/', level, name = 'level'),
    path('main/', main, name = 'main'),
    path('index/', index, name = 'index'),
    path('login/', log_in, name = 'login'),
    path('logout/', log_out, name = 'logout'),
    path('sign_up/', regestration, name = 'sign_up'),
    path('startup/', startup, name = 'startup'),
    path('practice/', practice, name = 'practice'),
    path('developer/', developer, name = 'developer'),
    path('users/', users, name = 'users'),
    path('', saving, name = 'saving'),
]