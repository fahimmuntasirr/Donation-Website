from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your views here.
def index(request):
    queryset = donation_list.objects.all()
    context = {'q' : queryset}
    return render(request, 'index.html',context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login_page/')
        
        user = authenticate( username = username, password = password)
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login_page/')

        else:
            login(request,user)
            print(user.first_name)
            return redirect('/')
    return render(request, 'login-page.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile_dp= request.FILES.get('profile_dp')
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
    
        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/signup/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        user_detail = user_details(
            user = user,
            profile_dp = profile_dp,
            date = date,
            gender = gender,
            address = address,
            donation_count = 0,
            donation_amount = 0
        )
        user_detail.save()
        messages.success(request, 'Account created Successfully')
        return redirect('/signup/')
    return render(request, 'sign-up1.html')


def donation_page(request,id):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        username = request.POST.get('username')
        donation_number = request.POST.get('donation_number')

        user = User.objects.filter(username = username).first()
        if user is not None:
            user_detail = user_details.objects.get(user=user)
            user_detail.donation_amount += int(amount)
            user_detail.donation_count += 1
            user_detail.save()
        
        donations = donation_list.objects.get(name = id)
        donations.raised += int(amount)
        donations.donation_number = donation_number
        donations.save()

        donation_details.objects.create(
            name = username,
            donation_number = donation_number,
            amount = amount,
            username = username
        )
        return redirect('/donation_success/')
    return render(request, 'donation-page.html')

def donation_success(request):

    return render(request, 'donation-success.html')

@login_required(login_url="/login_page/")
def profile(request,id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # profile_dp= request.FILES.get('profile_dp')
        date = request.POST.get('date')
        profile_dp = request.FILES.get('profile_dp')
        address = request.POST.get('address')
        description = request.POST.get('description')

        user = User.objects.get(username = id)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user1 = User.objects.filter(username=id).first()
        user_detail = user_details.objects.get(user = user1)
        user_detail.date = date
        if profile_dp:
            user_detail.profile_dp = profile_dp
        user_detail.address = address
        user_detail.description = description
        user_detail.save()
        return redirect('/')
    
    return render(request, 'profile.html')