from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import CustomUserCreation, LoginForm
from django.contrib.auth import authenticate, login, logout

def show_users(request):
    users = UserProfile.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)

def show_user(request, pk):
    user = UserProfile.objects.get(id=pk)
    if request.method == 'POST':
        follow_button = request.POST.get('follow_button')
        if follow_button == 'follow':
            request.user.profiles.friend_request.add(user.profiles)
        elif follow_button == 'unfollow' or follow_button == 'requested':
            request.user.profiles.friend_request.remove(user.profiles)
            request.user.profiles.follows.remove(user.profiles)
        else:
            print('page doesnt exist')

    follows = user.profiles.follows.exclude(user=user)
    follow_nums = len(follows)
    following = user.profiles.following.exclude(user=user)
    following_nums = len(following)
    context = {'user': user, 'follows': follows, 'followings': following, 'follow_nums': follow_nums, 'following_nums': following_nums}
    return render(request, 'single_user.html', context)

def friend_requests(request, pk=None):
    friend_requests = request.user.profiles.requested_by.all()
    if request.method == 'POST':
        friend_to_add_profile = UserProfile.objects.get(id=pk)
        if request.POST['value'] == 'Accept':
            friend_to_add_profile.profiles.follows.add(request.user.profiles)
            request.user.profiles.requested_by.remove(friend_to_add_profile.profiles)
        else:
            request.user.profiles.requested_by.remove(friend_to_add_profile.profiles)
            print(request.user.profiles.requested_by.all())
    context = {'friend_requests': friend_requests}
    return render(request, 'friend_request.html', context)

def register_user(request):
    if str(request.user) != 'AnonymousUser':
        return redirect('show_dweet')
    if request.method == 'POST':  
        form = CustomUserCreation(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = CustomUserCreation()
    context = {'form': form, 'message': 'register'}
    return render(request, 'reg_login.html', context)

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('show_dweet')
    context = {'form': form, 'message': 'login'}
    return render(request, 'reg_login.html', context)

def login_or_reg(request):
    return render(request, 'reg_login.html')

def logout_user(request):
    logout(request)
    return redirect('/users/login_or_reg')

