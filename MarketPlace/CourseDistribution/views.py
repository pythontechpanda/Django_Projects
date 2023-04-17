from django.shortcuts import render, redirect
from accounts.models import User
from MyAdmin.models import Profile
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control
import uuid
from django.conf import settings
from Supplier.models import CoursesOptions, LookingFor, Qualification, Country, State, City

# ===================================================================
# Create Admin Accounts By SuperUser

# Un :  mr@shubham123
# pass : 12345
# ===================================================================

def SignUp(request):
    if request.method == 'POST':
        name = request.POST['fname']
        # lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pwd']
        date = datetime.now()
        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/admin-register/')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/admin-register/')
            
            user_obj = User(first_name=name, email=email, username=username, password=make_password(password), is_admin=True, date_joined=date)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)
            return redirect('/admin-register/')
    else:
        return render(request, 'signup.html')
        




def SignUp_buyer(request):
    # print("Function Calling....")
    look = LookingFor.objects.all()
    qualifi = Qualification.objects.all()
    country = Country.objects.all()
    state = State.objects.all()
    if request.method == 'POST':
        name = request.POST['fname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pwd']
        qualification = request.POST['qualification']
        looks = request.POST['look']
        count = request.POST['country']
        sta = request.POST['state']
        # doc = request.FILES
        # resume = doc['upload_resume']
        date = datetime.now()
        # print("Function Calling....1")
        
        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/buyer-register/')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/buyer-register/')
            
            # print("Function Calling....2")
            user_obj = User(first_name=name,
                            email=email,
                            username=username,
                            password=make_password(password),
                            is_staff=True,
                            date_joined=date,
                            qualification=qualification,
                            looking_for=looks,
                            country=count,
                            state=sta,
                            # upload_resume=resume
                            )
            user_obj.set_password(password)
            user_obj.save()
            print("Function Calling....3")
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)
            return redirect('/buyer-register/')
    else:
        return render(request, 'signup.html', {'look':look, 'qualifi':qualifi, 'country':country, 'state':state})





def token_send(request):
    return render(request , 'token_send.html')

def success(request):
    return render(request , 'success.html')




def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/user-login/')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/user-login/')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')
    
    
    
    

def error_page(request):
    return  render(request , 'error.html')


def SignUp_supplier(request):
    prod = CoursesOptions.objects.all()
    country = Country.objects.all()
    state = State.objects.all()
    if request.method == 'POST':
        name = request.POST['fname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pwd']
        dp = request.FILES['profile_img']
        bg_img = request.FILES['backgroud_img']
        contact = request.POST['contact']
        company = request.POST['company']
        address = request.POST['address']
        product = request.POST['cource']
        official_email = request.POST['off_email']
        off_contact = request.POST['phone']
        count = request.POST['country']
        sta = request.POST['state']
        date = datetime.now()
        
       
        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/supplier-register/')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/supplier-register/')
            
            user_obj = User(first_name=name,
                            email=email,
                            username=username,
                            password=make_password(password),
                            is_supplier=True,
                            display_picture = dp,
                            bg_picture= bg_img,
                            contact_no = contact,
                            company_name = company,
                            address = address,
                            courses = product,
                            office_email = official_email,
                            off_phone_no = off_contact,
                            date_joined=date,
                            country=count,
                            state=sta
                            )
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)
            return redirect('/supplier-register/')
    else:
        return render(request, 'signup_supplier.html', {'prod':prod, 'country':country, 'state':state})

# ===================================================================

# Login for Superuser and Admin Account

# =================================================================== 
@cache_control(max_age=3600)
def login_sys(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        print(uname)
        
        user_obj = User.objects.filter(username = uname).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/user-login/')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/user-login/')
        user = authenticate(username=uname, password=pwd)
        # print(user.date_joined)

        if user:
            login(request, user)
            # if user.is_superuser:
            #     return redirect('/superadmin/')
            if user.is_staff:                                 # Admin
                return redirect('/buyer-app/')
            elif user.is_admin:
                return redirect('/admin-app/')
            elif user.is_supplier:
                return redirect('/supplier-app/')
            
        else:
            messages.warning(request, "Invalid Userid and password")
            return redirect('/user-login/')
    
    return render(request, "login.html")
	
@cache_control(max_age=3600)
def logout_call(request):
	logout(request)
	return redirect('/user-login/')      #homepage
    



def homepage(request):
    return render(request, "homepage.html")



def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://localhost:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    