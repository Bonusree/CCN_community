from django.urls import path
from . import views

urlpatterns = [
    path('notice/', views.notice, name='notice'),
    path('notice/add_notice', views.add_notice, name='add_notice'),
    path('notice/download/<int:notice_id>/', views.download_pdf, name='download_pdf'),
    path('notice/delete_notice/<int:notice_id>/', views.delete_notice, name='delete_notice'),
]