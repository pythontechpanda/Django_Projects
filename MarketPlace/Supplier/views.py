from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User, Follow
from Supplier.models import CoursesOptions, Country,State,City
from django.contrib import messages
from Supplier.models import *
from datetime import datetime
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import geocoder
import folium
from django.db.models import Q
from geopy.geocoders import Nominatim

def demo(request):
    getData = User.objects.get(id=request.user.id)
    all_post = CreatePost.objects.filter(author=getData).order_by("id").reverse()
    
    prod = CoursesOptions.objects.all()
    qualifi = Qualification.objects.all()
    country = Country.objects.all()
    state = State.objects.all()
    
    user = Follow.objects.filter(followed=getData)
    # for i in user:
    #    print(i.followed_by.first_name)
    # for count comment
    # getPost = CreatePost.objects.get(id=4)
    # count_comm = CommentForPost.objects.filter(post=getPost).count()
    # print(count_comm)
    
    
    return render(request, "supplier/index.html", {'mypost':all_post,
                                                   'prod':prod,
                                                   'qualifi':qualifi,
                                                   'country':country,
                                                   'state': state,
                                                   'follower':user
                                                   })



def getProfileData(request):
    current_user = User.objects.get(id=request.user.id)
    # print(current_user.username)
    posts = CreatePost.objects.filter(author=current_user).count()                      # count Total Posts
    posts_images = CreatePost.objects.filter(author=current_user).order_by("id").reverse()   # show all posted images
    # print("MY POSTs:  ", posts)
    user_followers = Follow.objects.filter(followed=current_user).count()     # Count total followers
    # print("MY Followers : ", user_followers)
    user = Follow.objects.filter(followed=current_user)
    print(user)
  

  
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
    
    #get user data
    data = User.objects.get(id=request.user.id)
    return render(request, "supplier/profile.html", {'data':data, 
                                                     'address':address,
                                                     "user_followers":user_followers,
                                                     'user':user, "num_of_posts":posts,
                                                     "posts_images":posts_images,
                                                     "myfollowers":user
                                                     })


def EditProfile(request):
    prod = CoursesOptions.objects.all()
    country = Country.objects.all()
    state= State.objects.all()
    if request.method == "POST":
        name = request.POST['fname']
        email = request.POST['email']
        username = request.POST['username']
        # dp = request.FILES['profile_img']
        # bg_img = request.FILES['backgroud_img']
        state = request.POST['state']
        country = request.POST['country']
        contact = request.POST['contact']
        company = request.POST['company']
        address = request.POST['address']
        product = request.POST['material']
        official_email = request.POST['off_email']
        off_contact = request.POST['phone']
        
        
        
        getData = User.objects.filter(id=request.user.id)
        getData.update(first_name=name,
                            email=email,
                            username=username,
                            is_supplier=True,
                            # display_picture = dp,
                            # bg_picture= bg_img,
                            country = country,
                            state = state,
                            contact_no = contact,
                            company_name = company,
                            address = address,
                            Materials = product,
                            office_email = official_email,
                            off_phone_no = off_contact,
                            )
        messages.success(request, 'Profile Updated Successfull.')
        return redirect("/supplier-app/profile-edit/")
       
    else:
        getData = User.objects.get(id=request.user.id)
        return render(request, "supplier/profile-edit.html", {'getData':getData,'prod':prod,'state':state,'country':country})
    
    
def AboutCompany(request):
    if request.method == "POST":
        name = request.POST['name']
        dp = request.FILES['profile_img']
        bg_img = request.FILES['backgroud_img']
        email = request.POST['email']
        service = request.POST['service']
        discrip = request.POST['discript']
        phone = request.POST['phone']
        user = request.user.id
        obj = CompanyProfile(name=name,display_picture=dp,bg_picture=bg_img,email=email,service=service,discription=discrip,contact=phone,created_by_id=user)
        obj.save()
        messages.success(request, "Company details create successfull.")
        return redirect('/supplier-app/company-details/')
    else:
        return render(request, 'supplier/company_profile.html')
    
    
def CompanyDetail(request):
    user = User.objects.get(id=request.user.id)
    # print(user)
    detail = CompanyProfile.objects.get(created_by_id=user)
    # print(detail)
    return render(request, "supplier/company_details.html", {'detail':detail})



def CompanyProfileEdit(request,id):
    if request.method == "POST":
        name = request.POST['name']
        dp = request.FILES.get('profile_img')
        bg_img = request.FILES.get('backgroud_img')
        email = request.POST['email']
        service = request.POST['service']
        discrip = request.POST['discript']
        phone = request.POST['phone']
        
        obj = CompanyProfile.objects.filter(id=request.user.id)
        obj.update(name=name,display_picture=dp,bg_picture=bg_img,email=email,service=service,discription=discrip,contact=phone)
        return redirect('/supplier-app/com-details/')
    else:
        obj = CompanyProfile.objects.get(id=id)
        print(obj.name)
        return render(request, "supplier/company_profile_edit.html", {'obj':obj})
    
    
# Working on Posts

def PostCreate(request):
    if request.method == "POST":
        discription = request.POST['discrip']
        post = request.FILES['image']
        created_by = request.user.id
        post_date = datetime.now()
        
        create = CreatePost(discription=discription, post_img=post,author_id=created_by,date=post_date)
        create.save()
        messages.success(request, "Post created successfull.")
        return redirect('/supplier-app/')
    else:
        getUser = User.objects.get(id=request.user.id)
        showPost = CreatePost.objects.filter(author=getUser)   
        return render(request, "supplier/post_create.html", {'mypost':showPost})
    
    
    
# def LikeViewSupplier(request):
#     print("Supplier call.....")
#     user = request.user
#     if request.method =="POST":
#         post_id = request.POST.get('post_id')
#         post_obj = CreatePost.objects.get(id=post_id)
        
#         if user in post_obj.like.all():
#             post_obj.like.remove(user)
#         else:
#             post_obj.like.add(user)
        
#         like, created =LikePost.Objects.get_or_create(user=user, post_id=post_id)
        
#         if not created:
#             if like.value == 'Like':
#                 like.value = 'Unlike'
#             else:
#                 like.value = 'Like'
                
#         like.save()
#     return redirect('/supplier-app/')
#     # return render(request, "supplier/index.html")
#     # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 




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
    return redirect('/supplier-app/')



# for helpfull or not 

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
    return redirect('/supplier-app/')

  
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
    return render(request, "supplier/comments.html", {'comment':comment,'getPost':getPost, 'numofComment':count_comm})
    
    

# # Searching functions
# def Searchbar(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         # print(q)
#         # data = Data.objects.filter(last_name__icontains=q)
#         multiple_q = Q(Q(first_name__icontains=q) | Q(option__icontains=q) | Q(option__icontains=q) | Q(country__icontains=q) | Q(state__icontains=q))
#         best = CreatePost.objects.filter(multiple_q)
#     else:
#         messages.info(request, "Not found....")
#         best = CreatePost.objects.filter(first_name="Pragati sharma")
#     return render(request, "supplier/index.html", {"best":best})
        
        
# def search(request):
#     queryset_list=CreatePost.objects.order_by('-list_data')

#     #keywords
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords:
#             queryset_list = queryset_list.filter(description__icontains = keywords)
        
#    #City
#     if 'city' in request.GET:
#         city = request.GET['city']
#         if city:
#             queryset_list=queryset_list.filter(city__iexact = city)

#      #State
#     if 'state' in request.GET:
#         state = request.GET['state']
#         if state:
#             queryset_list=queryset_list.filter(city__iexact = state)
    
    
#      # Bedrooms
#     if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms:
#             queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)
        
#      # Price
#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             queryset_list=queryset_list.filter(price__lte=price)
                
#     context={
#         'state_choices':state_choices,
#         'bedroom_choices':bedroom_choices,
#         'price_choices':price_choices,
#         'listings':queryset_list,
#         'values':request.GET,
#     }

#     return render(request, 'listings/search.html', context)




