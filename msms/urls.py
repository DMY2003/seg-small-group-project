"""msms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lessons import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('profile/', views.profile, name='profile'),
    path('password/', views.password, name='password'),
    path('log_out/', views.log_out, name='log_out'),

    path('administrator/lessons', views.admin_lessons, name='admin_lessons'),
    path('administrator/lessons/<int:lesson_id>', views.admin_lesson, name="admin_lesson"),
    path('administrator/delete_lesson/<int:lesson_id>', views.admin_lesson_delete, name='admin_lesson_delete'),
    path('administrator/requests', views.admin_requests, name='admin_requests'),
    path('administrator/delete_request/<int:request_id>', views.admin_request_delete, name='admin_request_delete'),
    path('administrator/requests/<int:request_id>', views.admin_request, name='admin_request'),
    path('director/create_admins', views.create_admins, name='create_admins'),
    path('director/manage_admins', views.manage_admins, name='manage_admins'),

    path('requests/', views.student_requests, name='student_requests'),
    path('requests/create', views.student_request_create, name='student_request_create'),
    path('requests/<int:request_id>', views.student_request_update, name='student_request_update'),
    path('delete_request/<int:request_id>', views.student_request_delete, name='student_request_delete'),
    path('lessons/', views.lessons, name='lessons'),
    path('transactions/', views.transactions, name='transactions'),
]

