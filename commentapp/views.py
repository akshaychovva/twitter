from django.shortcuts import render, redirect
from .models import Comment
from dweetapp.models import Dweet
from .forms import CommentForm
from django.urls import reverse

def comment(request, pk):
    dweet = Dweet.objects.get(id=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            new_comment = comment_form.save(commit=False)
            new_comment.dweet = dweet
            new_comment.user = request.user
            new_comment.save()
    comments = dweet.comment.all()
    form = CommentForm()
    context = {'comments': comments, 'form': form, 'dweet': dweet}
    return render(request, 'comments.html', context)

def update_comment(request, pk):
    '''
    Here we are updating and deleting comment
    '''
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        value = request.POST['value']
        if value == 'Update':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid:
                comment = form.save(commit=False)
                comment.save()
        elif value == 'Delete':
            comment.delete()
        return redirect(reverse('comment', kwargs={'pk': comment.dweet.id}))
    context = {'form': form, 'edit': 'edit', 'delete': 'delete', 'message': 'edit or delete'}
    return render(request, 'comments.html', context)

def like_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    profile = request.user.profiles
    if request.method == 'POST':
        like_value = request.POST.get("like_value")
        if like_value == 'Liked':
            comment.like_comment.remove(profile)
        else:
            comment.like_comment.add(profile)
        comment.save()
        return redirect(reverse('comment', kwargs={'pk': comment.dweet.id}))
    else:
        print('like form issue')



