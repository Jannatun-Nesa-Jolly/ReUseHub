from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name='home'), path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('items/new/', views.create_listing, name='create_listing'), path('items/<int:pk>/', views.detail, name='detail'),
    path('items/<int:pk>/edit/', views.edit_listing, name='edit_listing'),
    path('items/<int:pk>/complete/', views.complete_listing, name='complete_listing'),
    path('items/<int:pk>/save/', views.toggle_save, name='toggle_save'),
    path('items/<int:pk>/report/', views.report_listing, name='report_listing'), path('saved/', views.saved_items, name='saved_items'),
]
