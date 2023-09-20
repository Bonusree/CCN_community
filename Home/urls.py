from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('academic/', views.Academic, name='Academic'),
    path('routine/', views.Routine, name='Routine'),
    path('blood_community/', views.blood_community, name='Blood_community'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.LogoutPage, name='logout')
]