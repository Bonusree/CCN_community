from django.urls import path
from . import views

urlpatterns = [
    path('achievement/', views.achievement, name='achievement'),
    path('achievement/add-new', views.add_achievement, name='add_achievement'),
    path('achievement/delete-achievement/<int:ach_id>', views.delete_achievement, name='delete_achievement'),
]