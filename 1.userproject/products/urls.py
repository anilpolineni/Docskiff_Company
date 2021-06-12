from django.urls import path

from .views import home,register,additem,showitems

from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',home,name='home'),
	path('register',register,name="register"),
	path('login',auth_views.LoginView.as_view(template_name='products/login.html'),name="login"),
	path('logout',auth_views.LogoutView.as_view(template_name='products/logout.html'),name="logout"),
	path('additem',additem,name="additem"),
	path('showitems',showitems,name='showitems'),
	]