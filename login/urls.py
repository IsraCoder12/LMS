from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  
from login.views import home, user_login, dashboard, user_logout
from django.urls import path
from .views import signup 


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', home, name='home'),  
    path('login/', user_login, name='login'), 
    path('dashboard/', dashboard, name='dashboard'), 
    path("logout/", user_logout, name="logout"), 
    path("signup/", signup, name="signup"), 

    
    path('parent_dashboard/', include('parent_dashboard.urls')),


    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
