from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('academic/', views.Academic, name='Academic'),
    path('routine/', views.Routine, name='Routine'),
    path('blood_community/', views.blood_community, name='Blood_community'),
    path('alumni/', views.show_alumni, name='alumni'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile')
]