from django.urls import path
from . import views
urlpatterns =[
    path('',views.product_list,name='products'),
    path('register/',views.signup,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('dashboard/',views.products_dashboard,name='dashboard'),
    path('product_detail/<int:product_id>/',views.product_detail,name='product_detail'),
    path('update_product/<int:product_id>/',views.update_product,name='update_product'),
    path('delete/<int:product_id>/',views.delete_product,name='delete')
]