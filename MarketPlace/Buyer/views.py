from MyAdmin.models import Profile
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import User, Follow
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from Supplier.models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import geocoder
import folium
from django.db.models import Q
from geopy.geocoders import Nominatim
from ChatingApp.models import Thread


@login_required(login_url='signin')
def demo(request):
    # posts = CreatePost.objects.all().order_by("id").reverse()    
    
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    # print(address)
    # print('City:',address['city'])
    print('Country:',address['country'])
    
    # for following list
    user = User.objects.get(id=request.user.id)
    following_list = Follow.objects.filter(followed_by=user)
    # print(following_list)
    # for i in following_list:
    #     print(i.followed_by.display_picture)
    
    # post searching option
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(author__first_name__icontains=q) | Q(discription__icontains=q) | Q(date__icontains=q))
        posts = CreatePost.objects.filter(multiple_q)
    else:
        posts = CreatePost.objects.all().order_by("id").reverse()
    
    return render(request, "buyer/index.html", {'posts': posts, 'address':address,'following_list':following_list})


def profileSearch(request):
    # user = User.objects.filter(is_supplier=True)
    # print(user)
    
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(first_name__icontains=q) | Q(company_name__icontains=q) | Q(courses__icontains=q) | Q(country__icontains=q) | Q(state__icontains=q))
        data = User.objects.filter(multiple_q,is_supplier=True)
    else:
        data = User.objects.filter(is_supplier=True)
    context = {
        'data': data,
        # 'user':user
    }
    # posts = CreatePost.objects.all()
    return render(request, "buyer/search.html", context)



#===========This is for profile Update===========

@login_required(login_url='signin')
def profile_details(request):    
    if request.method == 'POST':
        address = request.POST['address']
        buying = request.POST['buy']
        looking = request.POST['looking']
        country = request.POST['country']
        state = request.POST['state']
        
        details = User.objects.filter(id=request.user.id)
        details.update(address=address, buying_op=buying, looking_for=looking, country=country, state=state)
        # details.save()
        messages.success(request, "Your Profile completed Enjoy MarketPlace Application.")
        return redirect('/buyer-app/')
    else:
        buy_op = Qualification.objects.all()
        look_for = LookingFor.objects.all()
        coun = Country.objects.all()
        sts = State.objects.all()
        user = User.objects.get(id=request.user.id)
              
        return render(request, "buyer/profile_complete.html", {'A':buy_op, 'B':look_for, 'C':coun, 'D':sts, 'user':user})



@login_required(login_url='signin')
def getProfileData(request):
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    # print(address)
    # print('City:',address['city'])
    print('Country:',address['country'])
    # get user data
    data = User.objects.get(id=request.user.id)
    return render(request, "buyer/profile.html", {'data':data, 'address':address})


@login_required(login_url='signin')
def EditStudentProfile(request):         
    look = LookingFor.objects.all()
    qualifi = Qualification.objects.all()
    country = Country.objects.all()
    state = State.objects.all()
    if request.method == 'POST':
        name = request.POST['fname']
        email = request.POST['email']
        username = request.POST['username']
        qualification = request.POST['qualification']
        looks = request.POST['look']
        count = request.POST['country']
        sta = request.POST['state']
        address = request.POST['address']
        contact = request.POST['contact']
        # dp = request.FILES['profile_img']
        profile_img = request.POST.get('profile_img')
        User.display_picture.url = profile_img
        
        
        
        getData = User.objects.filter(id=request.user.id)
        getData.update(first_name=name,
                            email=email,
                            username=username,
                            is_staff=True,
                            display_picture = profile_img,
                            # bg_picture= bg_img,
                            contact_no = contact,
                            qualification = qualification,
                            looking_for = looks,
                            country = count,
                            state = sta,
                            address = address,
                            )
        messages.success(request, 'Profile Updated Successfull.')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
       
    else:
        getData = User.objects.get(id=request.user.id)
        return render(request, "buyer/profile-edit.html", {'getData':getData,'look':look,'state':state,'country':country, 'qualifi':qualifi})


@login_required(login_url='signin')
def LikeView(request):
    # print("Buyer Calling......")
    user = request.user
    if request.method =="POST":
        post_id = request.POST.get('post_id')
        post_obj = CreatePost.objects.get(id=post_id)
        # profile = User.objects.get(user=request.user)
        
        
        if user in post_obj.like.all():
            post_obj.like.remove(user)
        else:
            post_obj.like.add(user)

        like, created = LikePost.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()
    return redirect('/buyer-app/')



# for helpfull or not 
@login_required(login_url='signin')
def InsightfulView(request):
    # print("Buyer Calling......")
    user = request.user
    if request.method =="POST":
        post_id = request.POST.get('post_id')
        post_obj = CreatePost.objects.get(id=post_id)
        # profile = User.objects.get(user=request.user)
        
        
        if user in post_obj.insightful.all():
            post_obj.insightful.remove(user)
        else:
            post_obj.insightful.add(user)

        insightful, created = InsightfulPost.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if insightful.value=='insightful':
                insightful.value='Uninsightful'
            else:
                insightful.value='insightful'
        else:
            insightful.value='insightful'

            post_obj.save()
            insightful.save()
    return redirect('/buyer-app/')

@login_required(login_url='signin')
def post_comment(request, id):
    if request.method == "POST":  # submit comment and then reload page
        user = request.user.id
        caption = request.POST['body']
        post_Id = id
        
        bio = CommentForPost(user_id=user, text=caption, post_id=post_Id)
        bio.save()
        
    getPost = CreatePost.objects.get(id=id)
    comment = CommentForPost.objects.all().filter(post=id)
    count_comm = CommentForPost.objects.all().filter(post=id).count()
    # print(count_comm)
    return render(request, "buyer/comments.html", {'comment':comment,'getPost':getPost, 'numofComment':count_comm})





# Code for Follow user By Shubham Raikwar

def view_user_information(request, username):
    account = get_object_or_404(User, username=username)
    getpost = CreatePost.objects.filter(author=account)
    num_post = CreatePost.objects.filter(author=account).count()
    print(getpost)
    following = False
    muted = None

    if request.user.is_authenticated:
        
        if request.user.id == account.id:
            return redirect("profile")

        followers = account.follower.filter(
        followed_by__id=request.user.id
        )
        if followers.exists():
            following = True
    
    if following:
        queryset = followers.first()
        if queryset.muted:
            muted = True
        else:
            muted = False

    context = {
        "account": account,
        "following": following,
        "muted": muted,
        'getpost':getpost,
        'num_post':num_post
    }
    return render(request, "buyer/follower.html", context)


@login_required(login_url = "login")
def follow_or_unfollow_user(request, user_id):
    followed = get_object_or_404(User, id=user_id)
    followed_by = get_object_or_404(User, id=request.user.id)

    follow, created = Follow.objects.get_or_create(
        followed=followed,
        followed_by=followed_by
    )

    if created:
        followed.follower.add(follow)

    else:
        followed.follower.remove(follow)
        follow.delete()

    return redirect("view_user_information", username=followed.username)



# communicate with chatting app

@login_required(login_url = "login")
def Chat_Thread(request, user_id):
    print("Thread Is calling....")
    first_person = get_object_or_404(User, id=user_id)
    second_person = get_object_or_404(User, id=request.user.id)
    
    print(first_person)
    print(second_person)
    thread_obj = Thread(first_person=first_person, second_person=second_person)
    thread_obj.save()
    
    return render(request, "chat1/chat-index.html")

# @login_required(login_url='login')
# def user_notifications(request):
#     notifications = Notificaiton.objects.filter(
#         user=request.user,
#         is_seen=False
#     )

#     for notification in notifications:
#         notification.is_seen = True
#         notification.save()
        
#     return render(request, 'notifications.html')


@login_required(login_url='login')
def mute_or_unmute_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    follower = get_object_or_404(User, pk=request.user.pk)
    instance = get_object_or_404(
        Follow,
        followed=user,
        followed_by=follower
    )

    if instance.muted:
        instance.muted = False
        instance.save()

    else:
        instance.muted = True
        instance.save()

    return redirect('view_user_information', username=user.username)

# def followers_count(request, id):
#     usr = CreatePost.objects.get(id=id)
#     # fol = Follow.objects.filter(followed=usr).count()
#     # print(fol)
   
#     return render(request, 'buyer/user_information.html', {'user':usr})



# def follow(request):
#     # print("Buyer Calling......")
#     user = request.user
#     if request.method =="POST":
#         post_id = request.POST.get('post_id')
#         post_obj = CreatePost.objects.get(id=post_id)
#         print("mypost Id: ", post_id)
#         # profile = User.objects.get(user=request.user)
        
        
#         if user in post_obj.followers.all():
#             post_obj.followers.remove(user)
#         else:
#             post_obj.followers.add(user)

#         follower, created = Follow.objects.get_or_create(user=user, post_id=post_id)

#         if not created:
#             if follower.value=='follower':
#                 follower.value='Unfollower'
#             else:
#                 follower.value='follower'
#         else:
#             follower.value='follower'

#             post_obj.save()
#             follower.save()
#     return redirect('/buyer-app/')







# def unfollow(request,id):
#     user = request.user
#     following = get_object_or_404(User, id=id)
#     Follow.objects.filter(user=user, following=following).delete()
#     return redirect(request.META.get('HTTP_REFERER'))



# def followers_count(request, id):
#     usr = CreatePost.objects.get(id=id)
#     # fol = Follow.objects.filter(followed=usr).count()
#     # print(fol)
#     if request.method == 'POST':
#         user = request.POST['user']
#         follower = request.POST['followed']
        
#         followers_cnt = Follow.objects.create(followed_id=follower, user_id=user)
#         followers_cnt.save()
#         print("Working follower")
#         # return redirect('/buyer-app/followers_count/')
#         return redirect(request.META.get('HTTP_REFERER'))
       
#     else:
#         current_user = request.user.id
#         print(current_user)
#         logged_in_user = request.user.username
#         user_followers = len(Follow.objects.filter(user=current_user))
#         user_following = len(Follow.objects.filter(followed=current_user))
#         user_followers0 = Follow.objects.filter(user=current_user)
#         user_followers1 = []
#         for i in user_followers0:
#             user_followers0 = i.followed
#             user_followers1.append(user_followers0)
#         if logged_in_user in user_followers1:
#             follow_button_value = 'unfollow'
#         else:
#             follow_button_value = 'follow'

#         print("my Followers",user_followers)
#         return render(request, 'buyer/follower.html', {
#             'current_user': current_user,
#             'user_followers': user_followers,
#             'user_following': user_following,
#             'follow_button_value': follow_button_value,
#             'user':usr
#         })

        # return render(request, 'buyer/follower.html')


# @login_required(login_url='signin')
# def followers_count(request, id):
#     data = CreatePost.objects.get(id=id)
#     print(data)
#     if request.method == 'POST':
#         value = request.POST['value']
#         user = request.POST['user']
#         follower = request.POST['follower']
        
#         if value == 'follow':
#             followers_cnt = FollowersCount(follower=follower, user_id=user)
#             followers_cnt.save()
#             print("Working follower")
#             return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
#         else:
#             followers_cnt = FollowersCount.objects.get(follower=follower, user=user)
#             followers_cnt.delete()
#             return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  
#     else:
#         followerCount =FollowersCount.objects.all().count()
#         current_user = request.user
#         print(current_user)
#         logged_in_user = request.user.username
#         user_followers = len(FollowersCount.objects.filter(user=current_user))
#         user_following = len(FollowersCount.objects.filter(follower=current_user))
#         user_followers0 = FollowersCount.objects.filter(user=current_user)
#         user_followers1 = []
#         for i in user_followers0:
#             user_followers0 = i.follower
#             user_followers1.append(user_followers0)
#         if logged_in_user in user_followers1:
#             follow_button_value = 'unfollow'
#         else:
#             follow_button_value = 'follow'

#         print(user_followers)
#         return render(request, 'buyer/follower.html', {
#             'current_user': current_user,
#             'user_followers': user_followers,
#             'user_following': user_following,
#             'follow_button_value': follow_button_value,
#             'follow_by_user':data,
#             'followerCount':followerCount
#         })


# @login_required(login_url='signin')
# def followers_count(request):
    
#     if request.method == 'POST':
#         value = request.POST['value']
#         user = request.POST['user']
#         follower = request.POST['follower']
        
#         if value == 'follow':
#             followers_cnt = FollowersCount.objects.create(follower=follower, user=user)
#             followers_cnt.save()
#             print("Working follower")
#             return redirect('/buyer-app/followers_count/')
#         else:
#             followers_cnt = FollowersCount.objects.get(follower=follower, user=user)
#             followers_cnt.delete()
#             return redirect('/buyer-app/followers_count/')  
#     else:
#         current_user = request.user
#         print(current_user)
#         logged_in_user = request.user.username
#         user_followers = len(FollowersCount.objects.filter(user=current_user))
#         user_following = len(FollowersCount.objects.filter(follower=current_user))
#         user_followers0 = FollowersCount.objects.filter(user=current_user)
#         user_followers1 = []
#         for i in user_followers0:
#             user_followers0 = i.follower
#             user_followers1.append(user_followers0)
#         if logged_in_user in user_followers1:
#             follow_button_value = 'unfollow'
#         else:
#             follow_button_value = 'follow'

#         print(user_followers)
#         return render(request, 'buyer/follower.html', {
#             'current_user': current_user,
#             'user_followers': user_followers,
#             'user_following': user_following,
#             'follow_button_value': follow_button_value
#         })

            
#         # return render(request, "buyer/follower.html")
