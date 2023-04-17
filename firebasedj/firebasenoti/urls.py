# from django.urls import path
# from .views import home

# urlpatterns = [
#     path('', home),

# ]


from django.urls import path
from . import views
urlpatterns = [
    # path('notifications/send/', views.send_push_notification),
    path('send-notification/', views.send_notification, name='send-notification'),
]