from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='post_details'),    
    path('profile_detail/', views.profile_details, name='form'),
    path('profile/',views.getProfileData, name="profile"),
    path('searching/', views.profileSearch, name='profileSearch'),
    path('profile-edit/', views.EditStudentProfile, name="myprofile"),
    path('like/', views.LikeView, name="like_post"),
    path('insightful/', views.InsightfulView, name="insight"),
    path('comment/<int:id>/', views.post_comment, name="comment"),
    path('view_user_information/<str:username>/', views.view_user_information, name="view_user_information"),
    path('follow_or_unfollow/<int:user_id>/', views.follow_or_unfollow_user, name='follow_or_unfollow_user'),
    path('mute_or_unmute_user/<int:user_id>/', views.mute_or_unmute_user, name='mute_or_unmute_user'),
    # path('chatthread/<int:user_id>/',views.Chat_Thread, name='chatthread')
    path('chatthread/<int:user_id>/',views.Chat_Thread, name='chatthread')
    
]
