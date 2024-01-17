
from django.urls import path

from store_app import views
app_name='store_app'

urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('form_submit/',views.form_submit,name='form_submit'),
    path('course/',views.course,name='course'),
    path('logout', views.logout, name='logout'),
    path('<slug:product_slug>/',views.dep_det,name='products_by_category'),
    path('<slug:product_slug>/',views.dep_det,name='product_category_detail'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]
