from django.urls import path
from . import views


urlpatterns = [
    
    path('adminregister/', views.SignUp),
    path('adminpanel/', views.login_sys),
    path('logout/', views.logout_call, name='logout'),
    
    
    path('', views.IndexPage),
    path('getalluser/', views.UserTableData),
    
    
    path('getallkyc/', views.UserKycPage),
    path('createkyc/', views.CreateUserKyc),
    path('editkyc/<int:id>/', views.UpdateUserKyc, name="update_kyc"),
    path('delete_kyc/<int:id>/', views.DeleteUserKyc, name='del_kyc'),
    path('kycdetail/<int:id>/', views.DetailUserKycView, name='view_kyc'),  
    
    path('verified/<int:id>/', views.UserVerification, name="nitify"),
    path('reject/<int:id>/', views.UserVerificationReject, name="nitifyrej"),     
    
    
    path('getallcustomercare/', views.CustomerCarePage),
    path('createcustomercare/', views.CustomerCareView),
    path('editcustomercare/<int:id>/', views.UpdateCustomerCare, name="update_service"),
    path('delete_customercare/<int:id>/', views.DeleteCustomerCare, name='del_service'),
    
    
    path('getallbanks/', views.BankDetailPage),
    path('createbankdetail/', views.CreateBankDetailView),
    path('editbank/<int:id>/', views.UpdateBankDetail, name="update_bank"),
    path('delete_bank/<int:id>/', views.DeleteBankDetail, name='del_bank'),
    
    
    path('createnewuser/', views.createUser),
    # path('editkyc/<int:id>/', views.UpdateInvite, name="update_kyc"),
    # path('delete_kyc/<int:id>/', views.DeleteInvite, name='del_kyc'),
    
    
    
    
    path('createcashwallet/', views.CreateCashWallet),
    path('getcashwallet/', views.CashWalletPage),
    path('editwallet/<int:id>/', views.UpdateCashWallet, name="update_wallet"),
    path('delete_wallet/<int:id>/', views.DeleteCashWallet, name='del_wallet'),
    
    
    path('getcashwithdraw/', views.WithdrawMoneyPage),
    path('withdrawamount/', views.CreateCashWithdraw),
    path('editwithdraw/<int:id>/', views.UpdateCashWithdraw, name="update_withdraw"),
    path('delete_withdraw/<int:id>/', views.DeleteCashWithdraw, name='del_withdraw'),
    
    
    path('getallround/', views.RoundsPage),
    path('editround/<int:id>/', views.UpdateRounds, name="update_round"),
    path('delete_round/<int:id>/', views.DeleteRound, name='del_round'),
    
    
    path('addmessage/', views.CreateIssue),
    path('getallissue/', views.IssuePage),
    path('editissue/<int:id>/', views.UpdateIssue, name="update_msg"),
    path('delete_issue/<int:id>/', views.DeleteIssue, name='del_msg'),
    
    
    path('getallservice/', views.CustomerCarePage),
    path('edituser/<int:id>/', views.UpdateUser, name="update_user"),
    path('delete_user/<int:id>/', views.DeleteUser, name='del_user'),
    
    
    path('createinvite/', views.CreateInvite),
    path('getallinvite/', views.InvitePage),
    path('editinvite/<int:id>/', views.UpdateInvite, name="update_inv"),
    path('delete_invite/<int:id>/', views.DeleteInvite, name='del_inv'),
    
    
    
    path('getclubbyuser/', views.GetClubByUserPage),
    path('creategetclubbyuser/', views.CreateGetClubByUserView),
    path('editclubbyuser/<int:id>/', views.UpdateGetClubByUser, name="update_clubusr"),
    path('delete_clubbyuser/<int:id>/', views.DeleteGetClubByUser, name='del_clubusr'),
    
    
    
    
    path('getcloseclub/', views.ClubClosedTimePage),
    path('creategetclubclose/', views.CreateGetClubCloseView),
    path('editclubclose/<int:id>/', views.UpdateGetClubClose, name="update_cls"),
    path('delete_clubclose/<int:id>/', views.DeleteGetClubClose, name='del_cls'),
    
    
    
    path('getavgtransfer/', views.AvgTrasferTimePage),
    path('creategettransfer/', views.CreateAvgTrasferTimeView),
    path('edittransfertime/<int:id>/', views.UpdateAvgTrasferTime, name="update_avg"),
    path('delete_transfertime/<int:id>/', views.DeleteAvgTrasferTime, name='del_avg'),
    
    path('getamttransfer/', views.AmountTrasferTimePage),
    path('createamttransfer/', views.CreateAmountTrasferTimeView),
    path('editamttransfer/<int:id>/', views.UpdateAmountTrasferTime, name="update_amt"),
    path('delete_amttransfer/<int:id>/', views.DeleteAmountTrasferTime, name='del_amt'),
    
    
    path('getnotification/', views.AppNotificationPage),
    # path('creategetclubbyuser/', views.CreateGetClubByUserView),
    # path('editclubbyuser/<int:id>/', views.UpdateGetClubByUser, name="update_clubusr"),
    # path('delete_clubbyuser/<int:id>/', views.DeleteGetClubByUser, name='del_clubusr'),
    
    
    path('getpaymentlist/', views.PaymentrecordPage),
    # path('creategetclubbyuser/', views.CreateGetClubByUserView),
    path('editpayment/<int:id>/', views.UpdatePaymentrecord, name="update_pay"),
    path('delete_payment/<int:id>/', views.DeletePaymentrecord, name='del_pay'),
    
    #------------user pending---------------
    
    
    
    
    # working on club
    path('createclub/', views.CreateClub),
    path('getallclub/', views.ClubPage),
    path('editclub/<int:id>/', views.UpdateClub, name="update_club"),
    path('delete_club/<int:id>/', views.DeleteClub, name='del_club'),
    path('clubdetail/<int:id>/', views.DetailClub, name='view'),
    path('inviteclub/<int:id>/<int:uid>/', views.inviteUser,name='invite'),
    
    path('userkycstatus/<int:kycid>/', views.UserKycNotification,name='userkycstatus'),
    
    # my_view
    # path('timernotification/', views.send_notification),  
    
    
]


