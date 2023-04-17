from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

from django.conf import settings  
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

# create router objects
router = DefaultRouter()
router.register('profile', views.UserCreation, basename='profile')
router.register('userkyc', views.userkycview, basename='userkyc')
router.register('bankaccount', views.bankdetailview, basename='bankaccount')
router.register('roundview', views.roundview, basename='roundview')
router.register('clubinvite', views.clubinvite, basename='clubinvite')
router.register('customercare', views.CustomerCareView, basename='customercare')
# router.register('userclub1', views.userclub, basename="userclub")
router.register('issuemessages', views.Issue_messages, basename='issuemessages')
router.register('issuelist', views.MentionView, basename="issuelist")
router.register('addmoney', views.AddMoneyView, basename="addmoney")
router.register('withdrawmoney', views.WithdrawAmountView, basename="withdrawmoney")
# router.register('getclubbyuser', views.GetClubByUserView, basename="getclubbyuser")
router.register('getbis', views.GetBidData, basename="getbis")
router.register('avgtransfer', views.AvgTrasferTimeView, basename="avgtransfer")
router.register('amounttransfer', views.AmountTrasferTimeView, basename="amounttransfer")
router.register('clubclosed', views.ClubClosedTimeView, basename="clubclosed")
router.register('notificationlist', views.AppNotificationView, basename="notificationlist")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('bslogin/',views.bslogin),
    path('club/',views.clubview),
    path('clubshow/<int:id>',views.clubviewupdate),
    path('userclub/<int:pk>',views.userclub),
    path('clubuser/<int:pk>',views.clubuser),
    path('homepage/', include("adminapp.urls")),
    path('my_view/', views.my_view,name='my_view'),
    path('send-notification/', views.clubinvite_notification, name='send-notification'),
    path('paymentremainder/<int:pk>',views.paymentremainder),
    # path('adminregister/', views.SignUp),
    # path('', views.login_sys),
    # path('logout/', views.logout_call, name='logout')
    
]





 

# urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:  
        urlpatterns     += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 