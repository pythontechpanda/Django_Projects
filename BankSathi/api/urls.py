from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# create router objects
router = DefaultRouter()
router.register('creditcard', views.CreditCardView, basename='creditcard')
router.register('demataccount', views.DematAccountsView, basename='demataccount')
router.register('investment', views.InvestmentsView, basename='investment')
router.register('itrandtax', views.ITRandTAXView, basename='itrandtax')
router.register('bankaccount', views.BankAccountsView, basename='bankaccount')
router.register('creditcard', views.CreditLineView, basename='creditcard')
router.register('personalloan', views.PersonalLoanView, basename='personalloan')
router.register('creditline', views.CreditLineView, basename='creditline')
router.register('personaldetail', views.PersonalDetailsView, basename='personaldetail')
router.register('registeruser', views.RegistrationView, basename='registeruser')
router.register('kycdetail', views.KYCDetailsView, basename='kycdetail')
router.register('likeview', views.LikeProductView, basename='likeview')


urlpatterns = [
  
    path('', include(router.urls)),
    
]
