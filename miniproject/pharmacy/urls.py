from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('medicine/<int:id>/', views.medicine_detail, name='medicine_detail'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    # ✅ New added paths for the features:
    path('cart/update/<int:id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:id>/', views.remove_cart, name='remove_cart'),
    path('upload-prescription/', views.upload_prescription, name='upload_prescription'),
    path('medicines/', views.medicine_list, name='medicine_list'),

]
