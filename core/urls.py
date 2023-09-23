from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm
from cart.views import add_to_cart, cart

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('shop/', views.shop, name='shop'),
    path('set_category/<int:category_id>/', views.set_category_session, name='set_category_session'),
    path('shop/get_toys_by_category/', views.get_toys_by_category, name='get_toys_by_category'),
    path('add_to_cart/<int:toy_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
]