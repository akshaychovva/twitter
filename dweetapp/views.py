from django.shortcuts import render, redirect
from .models import Dweet
from .forms import DweetForm
from twitterapp.models import UserProfile
from django.db.models import Q
from profileapp.models import Profiles

def show_dweet(request):
    '''
    showing dweets and adding dweets, and showing new friends
    '''
    
    dweets = Dweet.objects.all()
    if str(request.user) != 'AnonymousUser':
        follows_to_exclude = request.user.profiles.follows.all()
        add_friends = UserProfile.objects.exclude(Q(id__in=follows_to_exclude.values("id")))
        form = DweetForm()
        if request.method == 'POST':
            dweetform = DweetForm(request.POST)
            if dweetform.is_valid:
                dweet = dweetform.save(commit=False)
                dweet.user = request.user
                dweet.save()
        context = {'dweets': dweets, 'form': form, 'add_friends': add_friends}
        return render(request, 'dweets.html', context)

    context = {'dweets': dweets, 'login': 'login'}
    return render(request, 'dweets.html', context)

def update_dweet(request, pk):
    '''
    Here we are updating and deleting dweets
    '''
    dweet = Dweet.objects.get(id=pk)
    form = DweetForm(instance=dweet)
    if request.method == 'POST':
        value = request.POST['value']
        if value == 'Update':
            form = DweetForm(request.POST, instance=dweet)
            if form.is_valid:
                dweet = form.save(commit=False)
                dweet.user = request.user
                dweet.save()
        elif value == 'Delete':
            dweet.delete()
        return redirect('show_dweet')

    context = {'form': form, 'edit': 'edit', 'delete': 'delete', 'message': 'edit or delete'}
    return render(request, 'dweets.html', context)

def like(request, pk):
    dweet = Dweet.objects.get(id=pk)
    profile = request.user.profiles
    if request.method == 'POST':
        like_value = request.POST.get("like_value")
        if like_value == 'Liked':
            dweet.like.remove(profile)
        else:
            dweet.like.add(profile)
        dweet.save()
        return redirect('show_dweet')
    else:
        print('like form issue')


