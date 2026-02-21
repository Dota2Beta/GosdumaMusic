from django.urls import path

from .views import (
    RegisterView,
    UserLoginView,
    UserLogoutView,
    admin_panel,
    create_application,
    dashboard,
    update_application_status,
)

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('applications/new/', create_application, name='create_application'),
    path('admin-panel/', admin_panel, name='admin_panel'),
    path('admin-panel/<int:app_id>/status/', update_application_status, name='update_application_status'),
]
