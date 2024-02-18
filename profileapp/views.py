from django.shortcuts import render, redirect
from .models import Profiles
from django.db.models import Q

def my_friends(request):
    current_user = request.user.profiles
    my_friends = current_user.follows.exclude(id=current_user.id)
    friends_to_add = Profiles.objects.exclude(Q(id__in=my_friends.values('id')) | Q(id=current_user.user.id))
    context = {'my_friends': my_friends, 'friends_to_add': friends_to_add}
    return render(request, 'peoples.html', context)

def add_friend(request, pk):
    if request.method == 'POST':
        print('anothern afdsshdfv nsdfhj sd nsdvn dsvn m')
        if request.POST.get('follow_button') == 'follow':
            userprofile = request.user.profiles
            user_to_add = Profiles.objects.get(id=pk)
            userprofile.friend_request.add(user_to_add)
        else:
            userprofile = request.user.profiles
            user_to_add = Profiles.objects.get(id=pk)
            userprofile.follows.remove(user_to_add)
            userprofile.friend_request.remove(user_to_add)
        return redirect('profiles')

