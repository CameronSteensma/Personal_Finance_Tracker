from django.urls import path
from . import views
from transactions.views import reports_view

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    path('reports/', reports_view, name='reports'),
    path('admin/', views.admin_view, name='admin'),

    # Authentication routes (these views must exist in views.py)
    path('accounts/', views.accounts_view, name='accounts'),
    path('users/', views.users_view, name='users'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
