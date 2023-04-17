from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from Supplier.models import *
from django.contrib import messages

@login_required
def demo(request):
    sup_count = User.objects.filter(is_supplier=1).count()
    by_count = User.objects.filter(is_staff=1).count()
    print(sup_count)
    return render(request, "admin/dashboard.html", {'sup_count':sup_count,'by_count':by_count})


def add_country(request):
    # num_of_sup = User.objects.filter(is_supplier = 1).count()
    # a = User.objects.all()
    # print(a)
    data = Country.objects.all()
    if request.method == "POST":
        country = request.POST['name']
        
        if Country.objects.filter(country = country).first():
            messages.success(request, 'Country name is taken.')
            return redirect('/admin-app/country/')
        
        con_obj = Country(country=country)
        con_obj.save()
        messages.success(request, 'Country Added Successfull.')
    return render(request, "admin/country.html", {'data':data})



def add_state(request):
    data = Country.objects.all()
    show_st = State.objects.all()
    print(data)
    if request.method == "POST":
        state = request.POST['name']
        country = request.POST['country_id']
        
        
        if State.objects.filter(state = state).first():
            messages.success(request, 'State name is taken.')
            return redirect('/admin-app/state/')
        
        con_obj = State(state=state, con_id_id = country)
        con_obj.save()
        messages.success(request, 'State Added Successfull.')
    return render(request, "admin/state.html", {'data':data, 'show_st':show_st})



def add_city(request):
    data = State.objects.all()
    show_ct = City.objects.all()
    print(show_ct)
    # for i in show_ct:
    #     print(i.city, i.state, i.state.con_id)
    if request.method == "POST":
        city = request.POST['name']
        state = request.POST['state_id']
        
        if City.objects.filter(city = city).first():
            messages.success(request, 'City name is taken.')
            return redirect('/admin-app/city/')
        
        con_obj = City(city=city, state_id=state)
        con_obj.save()
        messages.success(request, 'City Added Successfull.')
    return render(request, "admin/city.html", {'data':data, 'show_ct':show_ct})


def User_list(request):
    user = User.objects.all()
    return render(request, "admin/users.html", {'user':user})


def MaterialOption(request):
    data = CoursesOptions.objects.all()

    if request.method == "POST":
        opt = request.POST['name']
        
        if CoursesOptions.objects.filter(opetion = opt).first():
            messages.success(request, 'Option already taken.')
            return redirect('/admin-app/material/')
        
        con_obj = CoursesOptions(opetion=opt)
        con_obj.save()
        messages.success(request, 'Option Added Successfull.')
    return render(request, "admin/materials.html", {'data':data})


def CoursesOptionsEdit(request, id):
    data = CoursesOptions.objects.all()
    if request.method == "POST":
        opt = request.POST['name']
        
        # if Qualification.objects.filter(opetion = opt).first():
        #     messages.success(request, 'Buying Option already taken.')
        #     return redirect('/admin-app/buying/')
        edit = CoursesOptions.objects.filter(id=id)
        edit.update(opetion=opt)
        messages.success(request, 'Material Option Updated')
        return redirect("/admin-app/material/") 
    else:
        data = CoursesOptions.objects.get(id=id)
        return render(request, "admin/materials_edit.html", {'data':data})


def MaterialOptionDelete(request, id):
    del_obj = CoursesOptions.objects.get(id=id)
    del_obj.delete()
    messages.success(request, 'Material Option Deleted!!')
    return redirect("/admin-app/material/") 





def BuyOption(request):
    data = Qualification.objects.all()

    if request.method == "POST":
        opt = request.POST['name']
        
        if Qualification.objects.filter(opetion = opt).first():
            messages.success(request, 'Buying Option already taken.')
            return redirect('/admin-app/buying/')
        
        con_obj = Qualification(opetion=opt)
        con_obj.save()
        messages.success(request, 'Buying Option Added Successfull.')
    return render(request, "admin/buy_option.html", {'data':data})


def BuyOptionEdit(request, id):
    data = Qualification.objects.all()
    if request.method == "POST":
        opt = request.POST['name']
        
        # if Qualification.objects.filter(opetion = opt).first():
        #     messages.success(request, 'Buying Option already taken.')
        #     return redirect('/admin-app/buying/')
        edit = Qualification.objects.filter(id=id)
        edit.update(opetion=opt)
        messages.success(request, 'Buying Option Updated')
        return redirect("/admin-app/buying/") 
    else:
        data = Qualification.objects.get(id=id)
        return render(request, "admin/buyer_edit.html", {'data':data})


def BuyOptionDelete(request, id):
    del_obj = Qualification.objects.get(id=id)
    del_obj.delete()
    messages.success(request, 'Buying Option Deleted!!')
    return redirect("/admin-app/buying/") 


def LookingOption(request):
    print("welcome")
    data = LookingFor.objects.all()
    
    print(data)

    if request.method == "POST":
        opt = request.POST['name']
        
        if LookingFor.objects.filter(opetion = opt).first():
            messages.success(request, 'Looking For already taken.')
            return redirect('/admin-app/looking/')
        
        con_obj = LookingFor(opetion=opt)
        con_obj.save()
        messages.success(request, 'Looking For Added Successfull.')
    return render(request, "admin/looking.html", {'data':data})


def LookingOptionEdit(request, id):
    data = LookingFor.objects.all()
    if request.method == "POST":
        opt = request.POST['name']
        
        # if Qualification.objects.filter(opetion = opt).first():
        #     messages.success(request, 'Buying Option already taken.')
        #     return redirect('/admin-app/buying/')
        edit = LookingFor.objects.filter(id=id)
        edit.update(opetion=opt)
        messages.success(request, 'Looking Option Updated')
        return redirect("/admin-app/looking/") 
    else:
        data = LookingFor.objects.get(id=id)
        return render(request, "admin/looking_edit.html", {'data':data})


def LookingOptionDelete(request, id):
    del_obj = LookingFor.objects.get(id=id)
    del_obj.delete()
    messages.success(request, 'Looking Option Deleted!!')
    return redirect("/admin-app/looking/") 