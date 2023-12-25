from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('tutorial/', views.tutorial, name='tutorial'),
    path('academic_notice/', views.academic_notice, name='academic_notice'),
    path('blood_community/', views.blood_community, name='Blood_community'),
    path('alumni/', views.show_alumni, name='alumni'),
    path('achievement/', views.achievement, name='achievement'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile')
]