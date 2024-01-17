
from django.urls import path

from login_action import views
app_name='login_action'

urlpatterns = [

    path('register',views.register,name='register'),

]