from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list,name='app1/list'),
    path('create/', views.member_create,name='app1/create'),
    path('edit/<int:id>', views.member_edit,name='app1/edit'),
    path('delete/<int:id>', views.member_delete,name='app1/delete'),
]