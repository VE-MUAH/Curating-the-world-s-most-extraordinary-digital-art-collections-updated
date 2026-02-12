from django.urls import path
from app import views

urlpatterns = [
    # urls for our app itself
    path('', views.IndexView.as_view(), name='index'),
    
    # urls for the various numbers
    path('<int:pk>/', views.DetailsView.as_view(), name='details'),

    path('register/', views.UserFormView.as_view(), name='userform'),
    
    path('audit/', views.LoginView.as_view(), name='login'), # Just preserving older patterns if any
    
    # Feature URLs
    path('add/', views.PieceCreateView.as_view(), name='add_piece'),
    path('edit/<int:pk>/', views.PieceUpdateView.as_view(), name='edit_piece'),
    path('delete/<int:pk>/', views.PieceDeleteView.as_view(), name='delete_piece'),
    
    # Auth URLs
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    # Admin Dashboard
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

]
