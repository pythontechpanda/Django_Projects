from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='homepage'),
    path('country/', views.add_country, name='country'),
    path('state/', views.add_state, name='state'),
    path('city/', views.add_city, name='city'),
    path('user/', views.User_list, name='user'),
    path('material/', views.MaterialOption, name='material'),
    path('buying/', views.BuyOption, name='buying'),
    path('looking/', views.LookingOption, name='looking'),
    
    # Edit all options
    path('material-edit/<int:id>/', views.CoursesOptionsEdit, name='edit_m'),
    path('buying-edit/<int:id>/', views.BuyOptionEdit, name='edit_b'),
    path('looking-edit/<int:id>/', views.LookingOptionEdit, name='edit_l'),
    
    # Delete all options
    path('material-delete/<int:id>/', views.MaterialOptionDelete, name='delete_m'),
    path('buying-delete/<int:id>/', views.BuyOptionDelete, name='delete_b'),
    path('looking-delete/<int:id>/', views.LookingOptionDelete, name='delete_l'),
    
]
