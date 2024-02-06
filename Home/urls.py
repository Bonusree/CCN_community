from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blood_community/', views.blood_community, name='Blood_community'),
    path('alumni/', views.show_alumni, name='alumni'),
    path('alumni/delete/<int:id>', views.delete_alumni, name='delete_alumni'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('manage-user/', views.manage_user, name='manage_user'),
    path('manage-user/delete/<int:id>', views.delete, name='user_delete'),
    path('manage-user/update_admin/<int:id>', views.update_admin, name='update_admin'),
    path('manage-user/approve_user/<int:id>', views.approve_user, name='update_admin')
]